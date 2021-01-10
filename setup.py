#!/usr/bin/env python
# coding: utf-8

# Modified based on https://github.com/ytdl-org/youtube-dl/blob/master/setup.py

from setuptools import setup

# pylint: disable=exec-used
exec(compile(open('mw2fcitx/version.py').read(), 'mw2fcitx/version.py', 'exec'))

DESCRIPTION = 'Build fcitx5 libraries from MediaWiki sites'

setup(name='mw2fcitx',
      # pylint: disable=undefined-variable
      version=__version__,
      description=DESCRIPTION,
      long_description=open("README.md", encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      url='https://github.com/outloudvi/mw2fcitx',
      author='Outvi V',
      author_email='oss@outv.im',
      license='Unlicense',
      include_package_data=True,
      packages=[
          'mw2fcitx',
          'mw2fcitx.dictgen',
          'mw2fcitx.tweaks',
          'mw2fcitx.exporters'
      ],
      install_requires=[
          "OpenCC>=1.1.1.post1",
          "pypinyin>=0.38.1",
      ],
      entry_points={'console_scripts': ['mw2fcitx = mw2fcitx.main:main', ]},
      classifiers=[
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Development Status :: 4 - Beta', 'Environment :: Console',
          'License :: Public Domain', 'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython'
      ])
