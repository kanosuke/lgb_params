# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='lgb_params',
    version='0.1.0',
    description='utility for parameters of lightgbm',
    author='kanosuke',
    author_email='',
    url='https://github.com/kanosuke/lgb_params',
    license='MIT',
    install_requires=['lightgbm', 'hyperopt'],
    packages=find_packages()
)

