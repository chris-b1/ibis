#!/usr/bin/env python

# Copyright 2014 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import setup, find_packages

import versioneer


LONG_DESCRIPTION = """
Ibis is a productivity-centric Python big data framework.

See http://ibis-project.org
"""

impala_requires = [
    'hdfs>=2.0.0',
    'impyla>=0.13.7',
    'sqlalchemy>=1.0.0',
    'thrift<=0.9.3',
    "thriftpy<=0.3.9; python_version < '3'",
]

sqlite_requires = ['sqlalchemy>=1.0.0']
postgres_requires = sqlite_requires + ['psycopg2']
kerberos_requires = ['requests-kerberos']
visualization_requires = ['graphviz']

all_requires = (
    impala_requires +
    postgres_requires +
    kerberos_requires +
    visualization_requires
)

develop_requires = all_requires + [
    'click',
    'flake8',
    "mock; python_version < '3'",
    "pytest>=3; python_version >= '3'",
    "pytest<3; python_version < '3'",
]

with open('requirements.txt', 'rt') as f:
    install_requires = list(map(str.strip, f))

setup(
    name='ibis-framework',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=install_requires,
    extras_require={
        'all': all_requires,
        'develop': develop_requires,
        'impala': impala_requires,
        'kerberos': kerberos_requires,
        'postgres': postgres_requires,
        'sqlite': sqlite_requires,
        'visualization': visualization_requires,
    },
    scripts=[
        os.path.join(
            os.path.dirname(__file__), 'scripts', 'test_data_admin.py'
        ),
    ],
    description="Productivity-centric Python Big Data Framework",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
    ],
    license='Apache License, Version 2.0',
    maintainer="Wes McKinney",
    maintainer_email="wes@cloudera.com"
)
