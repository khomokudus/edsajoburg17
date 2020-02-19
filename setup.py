from setuptools import setup, find_packages

setup(
    name='edsajoburg17',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='functions to calculate metrics using Eskom Data',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/khomokudus/edsajoburg17',
    author='EDSA_Joburg2020_Team_17',
    author_email= 'khomokudus@gmail.com'
)
