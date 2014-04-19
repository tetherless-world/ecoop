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
import subprocess

if sys.version_info[:2] < (2, 6) or (3, 0) <= sys.version_info[0:2] < (3, 2):
    raise RuntimeError("Python version 2.6, 2.7 or >= 3.2 required.")

if sys.version_info[0] >= 3:
    import builtins
else:
    import __builtin__ as builtins


CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: C
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""
AUTHOR              = 'epinux'
MAJOR               = 0
MINOR               = 1
MICRO               = 0
ISRELEASED          = False
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout = subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"
    #print(GIT_REVISION)
    return GIT_REVISION

GIT_REVISION = git_version()

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

def get_version_info():
    # Adding the git rev number needs to be done inside write_version_py(),
    # otherwise the import of numpy.version messes up the build under Python 3.
    FULLVERSION = VERSION
    #if os.path.exists('.git'):
    GIT_REVISION = git_version()
    if not ISRELEASED:
        FULLVERSION += '.dev-' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


def write_version_py(filename='lib/ecoop/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM ecoop SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    FULLVERSION, GIT_REVISION = get_version_info()

    a = open(filename, 'w')
    try:
        a.write(cnt % {'author' : AUTHOR,
                       'version': VERSION,
                       'full_version' : FULLVERSION,
                       'git_revision' : GIT_REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()


with open('README.md') as file:
    long_description = file.read()


write_version_py()

setup(
    name = 'ecoop',
    version = '0.1.0',
    description = 'A collecton of utilities to be used from inside an IPython Notebook to automatize the building of the Ecosystem Status Report for the NE-LME - Climate forcing UseCase',
    long_description=long_description,
    author = 'Massimo Di Stefano',
    author_unixid = 'epinux',
    author_email = 'epiesasha@me.com',
    url = 'http://github.com/epifanio/ecoop',
    packages = ['ecoop'],
    package_dir = {'': 'lib'},
    license = 'BSD 3-Clause license',
    platforms = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
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
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
)