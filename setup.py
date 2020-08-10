#!/usr/bin/env python
# coding: utf-8

# Modified based on https://github.com/ytdl-org/youtube-dl/blob/master/setup.py

import os.path
import warnings
import sys

try:
    from setuptools import setup, Command
    setuptools_available = True
except ImportError:
    from distutils.core import setup, Command
    setuptools_available = False
from distutils.spawn import spawn

exec(compile(open('mw2fcitx/version.py').read(), 'mw2fcitx/version.py', 'exec'))

DESCRIPTION = 'Build fcitx5 libraries from MediaWiki sites'

setup(name='mw2fcitx',
      version=__version__,
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      url='https://github.com/outloudvi/fcitx5-pinyin-moegirl',
      author='Outvi V',
      author_email='oss@outv.im',
      license='Unlicense',
      packages=[
          'mw2fcitx', 'mw2fcitx.exporters', 'mw2fcitx.utils', 'mw2fcitx.tweaks',
          'mw2fcitx.dictgen'
      ],
      classifiers=[
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Development Status :: 4 - Beta', 'Environment :: Console',
          'License :: Public Domain', 'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython'
      ])
