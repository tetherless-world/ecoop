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

version="2"
if [[ "$version" == "2" ]]
then pip=$PREFIX/bin/pip2.7
else pip=$PREFIX/bin/pip3.4
fi


echo "installing numexpr"
$pip install -U numexpr
echo "installing Cython"
$pip install -U Cython
echo "installing h5py"
$pip install -U h5py
echo "installing tables"
$pip install -U tables
echo "installing pandas"
$pip install -U pandas
echo "installing patsy"
$pip install -U patsy
echo "installing pysal"
$pip install -U pysal
echo "installing statsmodels"
$pip install -U statsmodels
echo "installing pyke"
$pip install -U pyke
echo "installing mock"
$pip install -U mock
echo "installing sqlalchemy"
$pip install -U sqlalchemy
echo "installing tempdir"
$pip install -U tempdir
echo "installing pysqlite"
$pip install -U pysqlite
echo "installing pycsw"
$pip install -U pycsw
echo "installing sympy"
$pip install -U sympy

echo "installing six"
$pip install -U six
echo "installing husl"
$pip install -U husl
echo "installing moss"
$pip install -U moss
echo "installing seaborn"
$pip install -U seaborn

echo "installing scikit-learn"
$pip install -U scikit-learn

echo "installing scikit-image"
$pip install -U scikit-image

echo "installing sympy"
$pip install -U sympy

echo "installing graphviz"
$pip install -U graphviz

#wget http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.36.0.tar.gz
#tar -zxvf graphviz-2.36.0.tar.gz
#cd graphviz-2.36.0
#./configure --prefix=$PREFIX
#make -j $np
#make install

echo "installing sh"
$pip install -U sh

echo "installing flask"
$pip install -U flask