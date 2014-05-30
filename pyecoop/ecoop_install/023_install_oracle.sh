#!/bin/sh

# assume root installed :
# yum install oracle-xe-11.2.0-1.0.x86_64.rpm
# is not open access (i've a local copy dw by oracle wit licens agreement)


version="2"
if [[ "$version" == "2" ]]
then python=$PREFIX/bin/python2.7
else python=$PREFIX/bin/python3.4
fi

export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe/
export LD_LIBRARY_PATH=/u01/app/oracle/product/11.2.0/xe/lib:$LD_LIBRARY_PATH
wget --no-check-certificate -c --progress=dot:mega http://softlayer-dal.dl.sourceforge.net/project/cx-oracle/5.1.2/cx_Oracle-5.1.2.tar.gz
tar -zxf cx_Oracle-5.1.2.tar.gz
cd cx_Oracle-5.1.2

$python setup.py install
rm -rf build
cd $TEMPBUILD
mv cx_Oracle-5.1.2.tar.gz $TEMPBUILD/tarball
mv cx_Oracle-5.1.2 $TEMPBUILD/src