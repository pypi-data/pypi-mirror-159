from pkg_resources import parse_requirements
import setuptools

setuptools.setup(
    name="PyEnzymeKinetics",
    version="1.1.2",
    url="https://github.com/haeussma/PyEnzymeKinetics",
    author="Haeussler, Max",
    author_email="max.haeussler@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=['lmfit==1.0.3',
                      'matplotlib==3.5.2',
                      'numpy==1.23.0',
                      'PyEnzyme==1.2.3',
                      'scipy==1.8.1']
)
