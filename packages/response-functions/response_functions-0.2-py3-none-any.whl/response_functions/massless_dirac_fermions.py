import numpy as np
from warnings import warn
from scipy.optimize import root_scalar
from scipy.special import gamma
from mpmath import polylog
from mpmath import exp as mpexp

class Massless_Dirac_Fermions():
    def __init__(self, 
    hv, 
    degeneracy, 
    density, 
    temperature, 
    dimension = 2, 
    maldague_sampling = None, 
    maldague_weights = None, 
    maldague_num = 101, 
    maldague_quadrature = 'gauss-legendre'):

        if dimension != 2:
            raise NotImplementedError('Only 2D Dirac Fermions available')
        self._dimension = dimension
        self._degeneracy = degeneracy
        self._hv = hv

        self._density = density
        self._temperature = temperature
        self._chemical_potential = self.compute_chemical_potential(density, temperature)

        self._kf = self.compute_fermi_wavevector(density)
        self._ef = self.compute_fermi_energy(density)

        self.maldague_num = maldague_num
        self.maldague_quadrature = maldague_quadrature
        self.maldague_sampling = maldague_sampling
        self.maldague_weights = maldague_weights

    # static properties
    @property
    def dimension(self):
        return self._dimension
    @dimension.setter
    def dimension(self, value):
        warn('dimension cannot be changed')

    @property
    def degeneracy(self):
        return self._degeneracy
    @degeneracy.setter
    def degeneracy(self, value):
        warn('degeneracy cannot be changed')
    #
    @property
    def hv(self):
        return self._hv
    @hv.setter
    def hv(self, value):
        warn('hv cannot be changed')

    ### dynamic properties
    @property
    def density(self):
        return self._density
    @density.setter
    def density(self, value):
        self._density = value
        self._chemical_potential = self.compute_chemical_potential(value, self._temperature)
        self._kf = self.compute_fermi_wavevector(self._density)
        self._ef = self.compute_fermi_energy(self._density)

    @property
    def chemical_potential(self):
        return self._chemical_potential
    @chemical_potential.setter
    def chemical_potential(self, value):
        self._chemical_potential = value
        self._density = self.compute_density(value, self._temperature)
        self._kf = self.compute_fermi_wavevector(self._density)
        self._ef = self.compute_fermi_energy(self._density)

    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self._chemical_potential = self.compute_chemical_potential(self._density, value)

    @property
    def kf(self):
        return self._kf
    @kf.setter
    def kf(self, value):
        warn('kf cannot be changed, change density instead')

    @property
    def ef(self):
        return self._ef
    @ef.setter
    def ef(self, value):
        warn('ef cannot be changed, change density instead')

    ### functions
    def compute_fermi_wavevector(self, density):
        return 2.*np.pi*np.power(
            abs(density)/(self._degeneracy * unit_sphere_volume(self._dimension)), 
            1./self._dimension)

    def compute_fermi_energy(self, density):
        return self._hv * np.sign(density) * self.compute_fermi_wavevector(density)

    def compute_chemical_potential(self, density, temperature):
        if temperature == 0.:
            return self.compute_fermi_energy(density)
        else:
            sol = root_scalar(lambda mu : self.compute_density(mu, temperature)-density, 
                              bracket = [0, self.compute_fermi_energy(density)] )
            return sol.root

    def compute_density(self, chemical_potential, temperature):
        if temperature == 0.: 
             return (
                 (self._degeneracy*unit_sphere_volume(self._dimension)/((2. *np.pi)**self._dimension))
                 *np.sign(chemical_potential) * (abs(chemical_potential) / self._hv)**self._dimension
                 )
        else:
            ne = (self._degeneracy/(2.*np.pi*self._hv**2)) * temperature**2 * fermi_dirac_int(1, chemical_potential/temperature)
            nh = (self._degeneracy/(2.*np.pi*self._hv**2)) * temperature**2 * fermi_dirac_int(1, -chemical_potential/temperature)
            return ne-nh

    def dos(self, energy):
        return (self._degeneracy/(2.*np.pi*self._hv**2)) * abs(energy)

    @staticmethod
    def G(z):
        z = z+0.j
        sz2m1 = np.sqrt(z-1.)*np.sqrt(z+1.)
        return z*sz2m1 - np.log(z + sz2m1)

    def polarization(self, omega, q, chemical_potential = None, temperature = None):
        '''polarization bubble. Identical to \chi_nn for \gamma=0'''
        if temperature is None:
            temperature = self.temperature
        if chemical_potential is None:
            chemical_potential = self.chemical_potential
            kf = self._kf
        else:
            kf = self.compute_fermi_wavevector(self.compute_density(chemical_potential, temperature))
        if temperature == 0.:
            omega = np.expand_dims(np.atleast_1d(omega),0)
            q = np.expand_dims(np.atleast_1d(q),1)
            Dplus  = (omega/self._hv + 2.*kf)/q
            Dminus = (omega/self._hv - 2.*kf)/q

            it1 = 8.*kf/(self._hv*q**2)
            it2 = (np.where(np.real(Dminus) < -1.,
                            self.G(-Dminus), # low w and low k
                            self.G(Dminus) + 1.j*np.pi  # high w or high k
                            )
                - self.G(Dplus)
                ) / np.sqrt(0.j + omega**2 - self._hv**2 * q**2)

            return np.squeeze(-self.degeneracy/(16*np.pi)*(it1+it2)*q**2)
        else:
            return average_maldague(lambda mu : self.polarization(omega = omega, q = q, chemical_potential= mu, temperature=0.),
             chemical_potential=chemical_potential, temperature=temperature,
             num = self.maldague_num, quadrature=self.maldague_quadrature, sampling = self.maldague_sampling, weights = self.maldague_weights)

    def chi_nn(self, omega, q, gamma = 0, chemical_potential = None, temperature = None):
        '''Density response. Decay rate \gamma taken into account via Mermin approximation '''
        assert(np.all(np.imag(omega)==0.))
        if gamma == 0.:
            return self.polarization(omega = omega, q=q, chemical_potential = chemical_potential, temperature = temperature)
        else:
            chi1 = self.polarization(omega = omega +1j*gamma, q=q, chemical_potential = chemical_potential, temperature = temperature)
            chi2 = self.polarization(omega = 0, q=q, chemical_potential = chemical_potential, temperature = temperature)
            omega = np.expand_dims(np.atleast_1d(omega),0)
            q = np.expand_dims(np.atleast_1d(q),1)
            chi2 = np.expand_dims(np.atleast_1d(chi2), 1)
            return (omega+1j*gamma)/(omega/chi1+1j*gamma/chi2)

    def chi_L(self, omega, q, chemical_potential = None, temperature = None):
        '''\chi_L(q,\omega) = \omega^2/q^2 \Pi(q,\omega) '''
        omega_ = np.expand_dims(np.atleast_1d(omega),0)
        q_ = np.expand_dims(np.atleast_1d(q),1)
        return np.squeeze(omega_**2/q_**2)*self.polarization( omega=omega, q=q, chemical_potential=chemical_potential, temperature=temperature)

    @staticmethod
    def G_T(z):
        z = z+0.j
        sz2m1 = np.sqrt(z-1.)*np.sqrt(z+1.)
        return z*sz2m1 + np.log(z + sz2m1)

    def chi_T(self, omega, q, chemical_potential = None, temperature = None):
        if temperature is None:
            temperature = self.temperature
        if chemical_potential is None:
            chemical_potential = self.chemical_potential
            kf = self._kf
        else:
            kf = self.compute_fermi_wavevector(self.compute_density(chemical_potential, temperature))
        if temperature == 0.:
            omega = np.expand_dims(np.atleast_1d(omega),0)
            q = np.expand_dims(np.atleast_1d(q),1)
            Dplus  = (omega/self._hv + 2.*kf)/q
            Dminus = (omega/self._hv - 2.*kf)/q

            it1 = 8.*kf/(self._hv*q**2)*omega**2
            it2 = (np.where(np.real(Dminus) < -1.,
                    self.G_T(-Dminus), # low w and low k
                    self.G_T(Dminus) - 1.j*np.pi  # high w or high k
                        )
            - self.G_T(Dplus)
            ) * np.sqrt(0.j + omega**2 - self._hv**2 * q**2) 

            return np.squeeze(self._degeneracy/(16 * np.pi) * (it1 + it2))
        else:
            return average_maldague(lambda mu : self.chi_T(omega = omega, q = q, chemical_potential= mu, temperature=0.),
             chemical_potential=chemical_potential, temperature=temperature,
             num = self.maldague_num, quadrature=self.maldague_quadrature, sampling = self.maldague_sampling, weights = self.maldague_weights)

    @staticmethod
    def theta(x, eta):
        if eta ==0.:
            return np.heaviside(x,0.5)
        else:
            return 0.5 +1/np.pi * np.arctan(x/eta)

    def conductivity(self, omega, gamma, chemical_potential = None, temperature = None):
        if temperature is None:
            temperature = self.temperature
        if chemical_potential is None:
            chemical_potential = self.chemical_potential
            ef = self._ef
        else:
            ef = self.compute_fermi_energy(self.compute_density(chemical_potential, temperature))
        if temperature == 0.:
            intraband = 1j/4.*abs(ef)/(omega+1j*gamma)
            interband = (np.pi/16.*self.theta(omega/(2.*abs(ef))-1,gamma)
                        +np.pi/16.*self.theta(-omega/(2.*abs(ef))-1,gamma)
                        +1j/32.*np.log(((2.*abs(ef)-omega)**2+gamma**2)/((2.*abs(ef)+omega)**2+gamma**2)) )
            return (intraband + interband) * self._degeneracy
        else:
            return average_maldague(lambda mu : self.conductivity(omega = omega, gamma = gamma, chemical_potential= mu, temperature=0.), 
            chemical_potential=chemical_potential, temperature=temperature,
            num = self.maldague_num, quadrature=self.maldague_quadrature, sampling = self.maldague_sampling, weights = self.maldague_weights)

    def non_local_conductivity(self, q, omega, gamma, chemical_potential = None, temperature = None):
        raise NotImplementedError('only local conductivity')