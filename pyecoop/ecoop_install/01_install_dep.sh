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

cd $TEMPBUILD
wget --no-check-certificate -c --progress=dot:mega http://www.hdfgroup.org/ftp/lib-external/szip/2.1/src/szip-2.1.tar.gz
tar -zxf szip-2.1.tar.gz
cd szip-2.1
./configure --prefix=$PREFIX/ --enable-shared
make -j $np
make install
make distclean > /dev/null 2>&1
cd $TEMPBUILD
#mv szip-2.1.tar.gz $TEMPBUILD/tarball
#mv szip-2.1 $TEMPBUILD/src

wget --no-check-certificate -c --progress=dot:mega http://www.hdfgroup.org/ftp/HDF/releases/HDF4.2.9/src/hdf-4.2.9.tar.gz
tar -zxf hdf-4.2.9.tar.gz
cd hdf-4.2.9
./configure --prefix=$PREFIX/ --enable-shared --disable-fortran --with-szlib=$PREFIX/ --enable-netcdf=no
make -j $np
make install
make distclean > /dev/null 2>&1
cd $TEMPBUILD
#mv hdf-4.2.9.tar.gz $TEMPBUILD/tarball
#mv hdf-4.2.9 $TEMPBUILD/src


wget --no-check-certificate -c --progress=dot:mega http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.13/src/hdf5-1.8.13.tar.gz
tar -zxf hdf5-1.8.13.tar.gz
cd hdf5-1.8.13
./configure --prefix=$PREFIX/ --enable-shared --enable-hl
make -j $np
make install
make distclean > /dev/null 2>&1
cd $TEMPBUILD
#mv hdf5-1.8.13.tar.gz $TEMPBUILD/tarball
#mv hdf5-1.8.13 $TEMPBUILD/src

wget --no-check-certificate -c --progress=dot:mega ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.3.2.tar.gz
tar -zxf netcdf-4.3.2.tar.gz
cd netcdf-4.3.2
LDFLAGS=-L$PREFIX/lib CPPFLAGS=-I$PREFIX/include ./configure --enable-netcdf-4 --enable-dap --enable-shared --prefix=$PREFIX
make -j $np
make install
make distclean > /dev/null 2>&1
cd $TEMPBUILD
#mv netcdf-4.3.2.tar.gz $TEMPBUILD/tarball
#mv netcdf-4.3.2 $TEMPBUILD/src


wget --no-check-certificate -c --progress=dot:mega ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.1.24.tar.gz
tar -zxf udunits-2.1.24.tar.gz
cd udunits-2.1.24
./configure --prefix=$PREFIX
make -j $np
make install
cd $TEMPBUILD
#mv udunits-2.1.24.tar.gz $TEMPBUILD/tarball
#mv udunits-2.1.24 $TEMPBUILD/src

wget --no-check-certificate -c --progress=dot:mega http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
tar -zxf cmake-2.8.12.2.tar.gz
cd cmake-2.8.12.2
./configure --prefix=$PREFIX
gmake
make install
make distclean > /dev/null 2>&1
cd $TEMPBUILD
#mv cmake-2.8.12.2.tar.gz $TEMPBUILD/tarball
#mv cmake-2.8.12.2 $TEMPBUILD/src