from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='Products.Members2FSD',
      version=version,
      description="scripts for managing people",
      long_description=open("README.rst").read() + "\n" + open("HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Carol McMasters-Stone',
      author_email='cbeck@ucdavis.edu',
      url='https://github.com/CMcStone/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
