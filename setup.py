from setuptools import setup, find_namespace_packages
import sys

setup(
    name='python_stl',
    version='1.0.0',
    url='https://github.com/wasserfeder/python-stl',
    license='MIT',
    maintainer='Cristian-Ioan Vasile',
    maintainer_email='crv519@lehigh.edu',
    description='A library for manipulating Signal Temporal Logic Formulae',
    packages=find_namespace_packages(include=['stl', 'stl.*']),
    install_requires=[
        "scipy"
    ]
)
