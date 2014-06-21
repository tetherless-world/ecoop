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

username <- Sys.getenv("USER")
localib <- paste("/home/",username,"/Envs/env1/lib64/R/library/",sep="")
.libPaths( c( .libPaths(), localib) )


core <- c("classInt", "DCluster", "deldir", "geoR", "gstat", "maptools",
"RandomFields", "raster", "RColorBrewer", "sp", "spatstat", "rgdal",
"spdep", "splancs","spgrass6", "rgeos","ncdf", "RSAGA", "data.table",
"mgcv", "bbmle", "emdbook", "MASS", "plyr","Rcpp")

packagelist <- core

for (i in packagelist) {
    install.packages(i, repos= "http://cran.rstudio.com/", lib = localib, dependencies=TRUE)
    output <- paste("Finished installing",i,sep=" ")
    print(output)
}

optional <- c("RPostgresql", "RSQLite", "RODBC", "data.table", "mgcv", "bbmle", "emdbook", "MASS", "plyr", "Rcpp", "ade4", "adehabitat", "adehabitatHR", "adehabitatHS", "adehabitatLT", "adehabitatMA", "ads", "akima", "ash", "aspace", "automap", "CircSpatial", "clustTool", "CompRandFld", "constrainedKriging", "cshapes", "diseasemapping", "DSpat", "ecespa", "fields", "FieldSim", "gdistance", "Geneland", "GEOmap", "geomapdata", "geonames", "geoRglm", "geosphere", "GeoXp", "glmmBUGS", "gmaps", "gmt", "Guerry", "hdeco", "intamap", "mapdata", "mapproj", "maps", "MarkedPointProcess", "MBA", "ModelMap", "ncf", "nlme", "pastecs", "PBSmapping", "PBSmodelling", "psgp", "ramps", "RArcInfo", "regress", "RgoogleMaps", "RPyGeo", "RSurvey", "rworldmap", "sgeostat", "shapefiles", "sparr", "spatcounts", "spatgraphs", "spatial", "spatialCovariance", "SpatialExtremes", "spatialkernel", "spatialsegregation", "spBayes", "spcosa", "spgwr", "sphet", "spsurvey", "SQLiteMap", "Stem", "tgp", "trip", "tripack", "tripEstimation", "UScensus2000", "vardiag", "vegan","ctv")
packagelist <- optional

for (i in packagelist) {
    install.packages(i, repos= "http://cran.rstudio.com/", lib = "/opt/ecoop/Envs/env1/lib/R/site-library/", dependencies=TRUE)
    output <- paste("Finished installing",i,sep=" ")
    print(output)
}

install.packages('ctv', repos= "http://cran.rstudio.com/", lib = localib, dependencies = TRUE)


q()