# -*- coding: utf-8 -*-
"""
ecoop
====

ecoop_ utility functions to automatize the building of the Ecosystem Status Report for the NE-LME.

.. _ecoop: https://github.com/epifanio/ecoop
.. _ecoop-project: http://tw.rpi.edu/web/project/ECOOP
"""


from distutils.core import setup
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


with open('README.md') as file:
    long_description = file.read()
    
setup(
    name = 'ecoop',
    version = '0.1.0',
    description = 'A collecton of utilities to be used from inside an IPython Notebook to automatize the building of the Ecosystem Status Report for the NE-LME - Climate forcing UseCase',
    long_description=long_description,
    author = 'Massimo Di Stefano',
    author_email = 'epiesasha@me.com',
    url = 'http://github.com/epifanio/ecoop',
    packages = ['ecoop'],
    package_dir = {'': 'lib'},
    license = 'BSD 3-Clause license',
    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
    ],
)