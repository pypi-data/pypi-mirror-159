import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "response_functions",
    version = "0.0",
    author = "Iacopo Torre",
    author_email = "iacopo.torre@icfo.eu",
    description = "",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://gitlab.com/itorre/response_functions",
    packages =setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires = ['numpy>=1.18.0', 'scipy', 'mpmath', 'matplotlib']
)