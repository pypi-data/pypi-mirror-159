#!/usr/bin/env python
# -*- coding:utf-8 -*-
#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################
from setuptools import setup, find_packages
setup(
    name="pyCeph",
    version="0.3.0",
    keywords=("pip", "pyCeph", "s3", "ceph"),
    description="ceph using tool",
    long_description="ceph using tool",
    license="MIT Licence",
    url="https://github.com/susufqx/pyCeph",
    author="susufqx",
    author_email="jiangsulirui@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "aioboto3>=9.6.0",
        "aiobotocore>=2.3.0",
        "aiohttp>=3.8.1",
        "aioitertools>=0.10.0",
        "aiosignal>=1.2.0",
        "async-timeout>=4.0.2",
        "asynctest>=0.13.0",
        "attrs>=21.4.0",
        "boto3>=1.24.29",
        "botocore>=1.27.29",
        "charset-normalizer>=2.1.0",
        "docutils>=0.15.2",
        "frozenlist>=1.3.0",
        "idna>=3.3",
        "jmespath>=0.10.0",
        "multidict>=6.0.2",
        "python-dateutil>=2.8.2",
        "s3transfer>=0.6.0",
        "six>=1.16.0",
        "typing_extensions>=4.3.0",
        "urllib3>=1.25.11",
        "wrapt>=1.14.1"
    ]
)
