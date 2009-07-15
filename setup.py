# -*- coding: utf-8 -*-
#
# © 2009, 2010 Digg, Inc. All rights reserved.
# Author: Ian Eure <ian@digg.com>
#

"""Setuptools definitions for replay."""

from setuptools import setup, find_packages

version = '1.0.0dev1'

setup(name='replay',
      version=version,
      description="Log replay tool.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Core Infrastructure',
      author_email='core@digg.com',
      url='http://github.com/digg/replay',
      license="Three-clause BSD",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      scripts=[],
      install_requires=[],
      extras_require = {
        'coverage': ["coverage"],
        'docs': ["epydoc", "markdown"]
        },
      tests_require=['nose'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
