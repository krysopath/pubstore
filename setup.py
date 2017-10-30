#!/usr/bin/env python3
# coding=utf-8
"""
Setupfile for tbx
"""
from setuptools import setup

setup(
    name='pubkey-storage',
    version='0.1b',
    description='nevermind',
    url='ssh://git@grumpy.crabdance.com:22222/home/git/pubkey-storage.git',
    author='Georg vom Endt',
    author_email='krysopath@gmail.com',
    license='GPL',
    packages=['pubstore', 'pubstore_client'],
    install_requires=[
        'flask', 'flask_restful',
        'sqlalchemy', 'PyYAML'
    ],
    zip_safe=False,
    scripts=["bin/pubstore", "bin/pubstore-server"]
)
