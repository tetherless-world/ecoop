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


CURRENTDIR=${PWD}
BUILD=epilib
PREFIX=/home/$USER/Envs/env1

TEMPBUILD=/home/$USER/$BUILD
mkdir -p $TEMPBUILD
mkdir -p $TEMPBUILD/tarball
mkdir -p $TEMPBUILD/src

cd $TEMPBUILD
export PATH=$PREFIX/bin:$PATH
export LD_LIBRARY_PATH=$PREFIX/lib:$PREFIX/lib64:$LD_LIBRARY_PATH


wget --no-check-certificate -c --progress=dot:mega \
  "https://software.ecmwf.int/wiki/download/attachments/3473437/grib_api-1.12.0.tar.gz"
tar xzf grib_api-1.12.0.tar.gz

cd grib_api-1.12.0
export CFLAGS="-O2 -fPIC"
./configure --enable-python --prefix=$PREFIX/ #--disable-numpy
make -j $np
make install
make distclean
cd $TEMPBUILD
#mv grib_api-1.12.0.tar.gz $TEMPBUILD/tarball
#mv grib_api-1.12.0 $TEMPBUILD/src

echo "$PREFIX/lib/python3.4/site-packages/grib_api" > gribapi.pth
cp gribapi.pth $PREFIX/lib/python3.4/site-packages/

git clone https://github.com/activepapers/activepapers-python.git
cd activepapers-python
$PREFIX/bin/python3.4 setup.py install
rm -rf build
cd $TEMPBUILD
#mv activepapers-python $TEMPBUILD/src