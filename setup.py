from setuptools import setup, find_packages

setup(
    name='Modelo_Estandar',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'PyQt5',
    ],
    description='A package modeling particles from the Standard Model with analysis and GUI tools.',
    author='Your Name',
)
