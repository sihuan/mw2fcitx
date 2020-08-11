#!/usr/bin/env python
# coding: utf-8

# Modified based on https://github.com/ytdl-org/youtube-dl/blob/master/setup.py

import os.path
import warnings
import sys
from setuptools import setup, Command, find_packages

exec(compile(open('mw2fcitx/version.py').read(), 'mw2fcitx/version.py', 'exec'))

DESCRIPTION = 'Build fcitx5 libraries from MediaWiki sites'

setup(name='mw2fcitx',
      version=__version__,
      description=DESCRIPTION,
      long_description=open("README.md", encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      url='https://github.com/outloudvi/fcitx5-pinyin-moegirl',
      author='Outvi V',
      author_email='oss@outv.im',
      license='Unlicense',
      include_package_data=True,
      packages=find_packages(),
      entry_points={'console_scripts': ['mw2fcitx = mw2fcitx.main:main',]},
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
