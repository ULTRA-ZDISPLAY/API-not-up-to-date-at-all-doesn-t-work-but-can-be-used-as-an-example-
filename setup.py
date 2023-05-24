from setuptools import find_packages, setup

setup(
    name='zdisplayapi',
    packages=find_packages(include=['zdisplayapi']),
    version='0.1.0',
    description='Librairie pour l\'api de ZDisplay.fr',
    author='DreWen',
    install_requires=['requests'], 
    setup_requires=[]
)
