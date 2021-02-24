#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os import path
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup



wrkDir = path.abspath(path.dirname(__file__))
with open(path.join(wrkDir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pycubedoe',
    version='0.1.3',
    license='LGPL-3.0-or-later',
    description='Generates design of experiements by constructing a nearly orthogonal latin hypercube with user-defined factors and appropriate factor ranges.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Travis Hartman',
    author_email='travis@jataware.com',
    url='https://github.com/jataware/pycubedoe',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    project_urls={

        'Changelog': 'https://github.com/jataware/pycubedoe/blob/master/CHANGELOG.md',
        'Issue Tracker': 'https://github.com/jataware/pycubedoe/issues',
    },
    keywords=['design of experiements', 'DOE', 'hypercube', 'latin hypercube', 'design point'],

    python_requires='>=3.6',
    
    install_requires=['pandas>=0.24.2'],
    extras_require={ "dev": ["pytest>=3.7", "twine>=3.3.0"]},
    setup_requires=[
        'pytest-runner',
    ],

)
