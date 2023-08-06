from pkg_resources import parse_requirements
import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    print(requirements)

setuptools.setup(
    name="PyEnzymeKinetics",
    version="1.1.5",
    url="https://github.com/haeussma/PyEnzymeKinetics",
    author="Haeussler, Max",
    author_email="max.haeussler@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=requirements
)