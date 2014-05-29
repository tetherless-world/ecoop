#!/bin/bash

###############################################################################
#
#
# Project: ECOOP, sponsored by The National Science Foundation
# Purpose: this code is part of the Cyberinfrastructure developed for the ECOOP project
#                http://tw.rpi.edu/web/project/ECOOP
#                from the TWC - Tetherless World Constellation
#                            at RPI - Rensselaer Polytechnic Institute
#                            founded by NSF
#
# Author:   Massimo Di Stefano , distem@rpi.edu -
#                http://tw.rpi.edu/web/person/MassimoDiStefano
#
###############################################################################
# Copyright (c) 2008-2014 Tetherless World Constellation at Rensselaer Polytechnic Institute
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################


PREFIX=/home/$USER/Envs/env1

export PATH=$PREFIX/bin:$PATH
export LD_LIBRARY_PATH=$PREFIX/lib:$PREFIX/lib64:$LD_LIBRARY_PATH

echo "installing h5py"
$PREFIX/bin/pip install -U h5py
echo "installing numexpr"
$PREFIX/bin/pip install -U numexpr
echo "installing Cython"
$PREFIX/bin/pip install -U Cython
echo "installing tables"
$PREFIX/bin/pip install -U tables
echo "installing pandas"
$PREFIX/bin/pip install -U pandas
echo "installing patsy"
$PREFIX/bin/pip install -U patsy
echo "installing pysal"
$PREFIX/bin/pip install -U pysal
echo "installing statsmodels"
$PREFIX/bin/pip install -U statsmodels
echo "installing pyke"
$PREFIX/bin/pip install -U pyke
echo "installing mock"
$PREFIX/bin/pip install -U mock
echo "installing sqlalchemy"
$PREFIX/bin/pip install -U sqlalchemy
echo "installing tempdir"
$PREFIX/bin/pip install -U tempdir
echo "installing pysqlite"
$PREFIX/bin/pip install -U pysqlite
echo "installing pycsw"
$PREFIX/bin/pip install -U pycsw
echo "installing sympy"
$PREFIX/bin/pip install -U sympy

echo "installing six"
$PREFIX/bin/pip install -U six
echo "installing husl"
$PREFIX/bin/pip install -U husl
echo "installing moss"
$PREFIX/bin/pip install -U moss
echo "installing seaborn"
$PREFIX/bin/pip install -U seaborn

echo "installing scikit-learn"
$PREFIX/bin/pip install -U scikit-learn

echo "installing scikit-image"
$PREFIX/bin/pip install -U scikit-image

echo "installing sympy"
$PREFIX/bin/pip install -U sympy