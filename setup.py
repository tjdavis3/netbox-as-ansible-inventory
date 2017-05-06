#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Copyright 2017, Ahmed AbouZaid <http://aabouzaid.com/>
# setup.py file is part Netbox dynamic inventory script.
# https://github.com/AAbouZaid/netbox-as-ansible-inventory

from setuptools import setup, find_packages
from codecs import open
from os import path


def open_file(file_name, splitlines=False):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, file_name), encoding='utf-8') as opened_file:
        file_output = opened_file.read()
    if splitlines:
        return file_output.splitlines()
    else:
        return file_output

# Get vars from project files.
version = open_file('VERSION')
long_description = open_file('README.rst')
main_requirements = open_file('requirements.txt', splitlines=True)
tests_requirements = open_file('tests/requirements.txt', splitlines=True)

setup(
    name='ansible-netbox-inventory',
    version=version,
    description='Ansible dynamic inventory script for Netbox',
    long_description=long_description,
    url='https://github.com/AAbouZaid/netbox-as-ansible-inventory',
    author='Ahmed AbouZaid',
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    keywords=['ansible', 'netbox', 'inventory'],
    install_requires=main_requirements,
    extras_require={
        'test': tests_requirements,
    },
)
