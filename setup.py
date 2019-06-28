import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='k2_core',
    version='0.0.26',
    author_email='simon.emmott@yahoo.co.uk',
    author='Simon Emmott',
    description='The core functionality for the K2 IDE service',
    packages=[
        'k2_core', 
        'k2_core.mixins', 
        'tests'
    ],
    long_description=read('README.md'),
    install_requires=[
    ],
)