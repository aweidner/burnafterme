#!/usr/bin/env python

from setuptools import setup, find_packages


def requirements_file_to_list(fn="requirements.txt"):
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name="burnafterme",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements_file_to_list(),
    package_data={},
    author="Adam Weidner",
    author_email="aweidner6993@gmail.com",
    description="Small service to expose redis as a temporary file server",
    license="MIT"
)
