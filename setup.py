#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='pycubedoe',
    version='0.0.1',
    license='LGPL-3.0-or-later',
    description='Generate ssdesign of experiements by constructing a nearly orthogonal latin hypercube with user-defined factors and appropriate factor ranges.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Travis Hartman',
    author_email='travis@jataware.com',
    url='https://github.com/travis-jat/python-pycubedoe',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Changelog': 'https://github.com/travis-jat/python-pycubedoe/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/travis-jat/python-pycubedoe/issues',
    },
    keywords=['design of experiements', 'DOE', 'hypercube', 'latin hypercube', 'design point'],

    python_requires='>=3.6',
    
    install_requires=['pandas>=0.24.2'],
    extras_require={ "dev": ["pytest>=3.7"]},
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        'console_scripts': [
            'pycubedoe = pycubedoe.cli:main',
        ]
    },
)
