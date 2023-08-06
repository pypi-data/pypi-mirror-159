from setuptools import setup, find_packages
import os

version = '2.0.0'

setup(name='collective.filteredlocking',
      version=version,
      description="A new specific permission that allows unlock of Plone contents",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone plonegov lock webdav',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://github.com/PloneGov-IT/collective.filteredlocking',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.locking',
          'plone.app.testing', #???
      ],
      extras_require={
          'test': [
              'plone.app.testing[robot]',
              'plone.app.robotframework',
              'plone.app.contenttypes',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
