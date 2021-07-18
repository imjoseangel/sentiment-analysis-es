#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0120

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import codecs
from glob import glob
import os
from os.path import abspath, dirname, normpath
from shutil import rmtree
from setuptools import setup, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = ('./build', './dist', './*.pyc',
                   './*.tgz', './*.egg-info', './.pytest_cache',
                   '.benchmarks', './tests/__pycache__',
                   './sentiment-analysis-es/__pycache__',
                   './__pycache__')

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        here = normpath(abspath(dirname(__file__)))

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob(os.path.normpath(
                os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError(
                        "%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                rmtree(path)


def read(rel_path):

    here = normpath(abspath(dirname(__file__)))

    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('VERSION'):
            delim = '?= '
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='sentiment-analysis-es',
    description='Spanish Sentiment Analysis using Multinomial Naive Bayes',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version=os.environ.get('SENTIMENTANALYSISES_VERSION', '0.0.0'),
    keywords='powerline k8s kubernetes status prompt',
    license='MIT',
    author='Jose Angel Munoz',
    author_email='josea.munoz@gmail.com',
    url='https://github.com/imjoseangel/sentiment-analysis-es',
    packages=['sentiment-analysis-es'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Utilities'
    ],
    install_requires=[
    ],
    cmdclass={
        'clean': CleanCommand,
    }
)
