#/usr/bin/env python
# -*- coding: utf-8 -*-

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


"""
Dictionary to store pair key-value to map the ECOOP CMAP

"""


ecooProvDict = {}

ecooProvDict['IPythonNotebook'] = {}
ecooProvDict['IPythonNotebook']['title'] = ''
ecooProvDict['IPythonNotebook']['description'] = ''
ecooProvDict['IPythonNotebook']['accessURL'] = ''


ecooProvDict['IPythonNotebookRun'] = {}
ecooProvDict['IPythonNotebookRun']['description'] = ''
ecooProvDict['IPythonNotebookRun']['startedAtTime'] = ''
ecooProvDict['IPythonNotebookRun']['endedAtTime'] = ''
ecooProvDict['IPythonNotebookRun']['wasAssociatedWith'] = ''


ecooProvDict['Cell'] = {}
ecooProvDict['Cell']['title'] = ''
ecooProvDict['Cell']['description'] = ''
ecooProvDict['Cell']['accessURL'] = ''

ecooProvDict['CellRun'] = {}
ecooProvDict['CellRun']['title'] = ''
ecooProvDict['CellRun']['description'] = ''
ecooProvDict['CellRun']['startedAtTime'] = ''
ecooProvDict['CellRun']['endedAtTime'] = ''
ecooProvDict['CellRun']['wasAssociatedWith'] = ''


ecooProvDict['Document'] = {}
ecooProvDict['Document']['title'] = ''
ecooProvDict['Document']['description'] = ''
ecooProvDict['Document']['downloadURL'] = ''


ecooProvDict['Dataset'] = {}
ecooProvDict['Dataset']['agent'] = ''
ecooProvDict['Dataset']['title'] = ''
ecooProvDict['Dataset']['description'] = ''
ecooProvDict['Dataset']['distribution'] = {}
ecooProvDict['Dataset']['distribution']['title'] = ''
ecooProvDict['Dataset']['distribution']['description'] = ''
ecooProvDict['Dataset']['distribution']['accessURL'] = ''
ecooProvDict['Dataset']['distribution']['downloadURL'] = ''
ecooProvDict['Dataset']['wasAttributedTo'] = ''

ecooProvDict['Dataset']['identifier'] = ''
ecooProvDict['Dataset']['license'] = {}
ecooProvDict['Dataset']['license']['LicenseDocument'] = ''
ecooProvDict['Dataset']['license']['MediaTypeOrExtent'] = ''
ecooProvDict['Dataset']['license']['LinguisticSystem'] = ''
ecooProvDict['Dataset']['format'] = ''
ecooProvDict['Dataset']['language'] = ''
ecooProvDict['Dataset']['byteSize'] = ''
ecooProvDict['Dataset']['generatedAtTime'] = ''
ecooProvDict['Dataset']['issued'] = ''
ecooProvDict['Dataset']['modified'] = ''
ecooProvDict['Dataset']['contactpoint'] = ''

ecooProvDict['Dataset']['SpatialExtents'] = {}
ecooProvDict['Dataset']['SpatialExtents']['extentTypeCode'] = ''
ecooProvDict['Dataset']['SpatialExtents']['westBoundLongitude'] = ''
ecooProvDict['Dataset']['SpatialExtents']['eastBoundLongitude'] = ''
ecooProvDict['Dataset']['SpatialExtents']['southBoundLatitude'] = ''
ecooProvDict['Dataset']['SpatialExtents']['northBoundLatitude'] = ''

ecooProvDict['Dataset']['TemporalExtens'] = {}
ecooProvDict['Dataset']['TemporalExtens']['startedAtTime'] = ''
ecooProvDict['Dataset']['TemporalExtens']['endedAtTime'] = ''

ecooProvDict['Dataset']['SpatialResolution'] = {}
ecooProvDict['Dataset']['SpatialResolution']['resolution'] = ''
ecooProvDict['Dataset']['SpatialResolution']['equivalentScale'] = ''

ecooProvDict['Dataset']['TemporalResolution'] = {}
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit'] = ''

"""
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit'] = {}
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitYear'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitMonth'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitWeek'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitDay'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitHour'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitMinute'] = ''
ecooProvDict['Dataset']['TemporalResolution']['temporalUnit']['unitSecond'] = ''
"""

"""
ecooProvDict['Dataset']['instrument'] = ''
ecooProvDict['Dataset']['algorithm'] = ''
ecooProvDict['Dataset']['model'] = ''

ecooProvDict['Dataset']['dataCenter'] = {}
ecooProvDict['Dataset']['dataCenter']['group'] = ''
ecooProvDict['Dataset']['dataCenter']['organization'] = ''
"""



ecooProvDict['Person'] = {}
ecooProvDict['Person']['name'] = ''
ecooProvDict['Person']['familyName'] = ''
ecooProvDict['Person']['givenName'] = ''
ecooProvDict['Person']['mbox'] = ''
ecooProvDict['Person']['phone'] = ''
ecooProvDict['Person']['address'] = ''
ecooProvDict['Person']['homepageURL'] = ''
ecooProvDict['Person']['isMemberOf'] = {}
ecooProvDict['Person']['isMemberOf']['Organization'] = ''
ecooProvDict['Person']['isMemberOf']['Group'] = ''



ecooProvDict['Organization'] = {}
ecooProvDict['Organization']['name'] = ''
ecooProvDict['Organization']['mbox'] = ''
ecooProvDict['Organization']['phone'] = ''
ecooProvDict['Organization']['address'] = ''
ecooProvDict['Organization']['homepageURL'] = ''
ecooProvDict['Organization']['hasMemberOf'] = {}
ecooProvDict['Organization']['hasMemberOf']['Person'] = ''
ecooProvDict['Organization']['hasMemberOf']['Group'] = ''


ecooProvDict['Group'] = {}
ecooProvDict['Group']['name'] = ''
ecooProvDict['Group']['mbox'] = ''
ecooProvDict['Group']['phone'] = ''
ecooProvDict['Group']['address'] = ''
ecooProvDict['Group']['homepageURL'] = ''
ecooProvDict['Group']['hasMemberOf'] = {}
ecooProvDict['Group']['hasMemberOf']['Person'] = ''
ecooProvDict['Group']['hasMemberOf']['Group'] = ''
ecooProvDict['Group']['isMemberOf'] = {}
ecooProvDict['Group']['isMemberOf']['Organization'] = ''



ecooProvDict['Library'] = {}
ecooProvDict['Library']['title'] = ''
ecooProvDict['Library']['description'] = ''
ecooProvDict['Library']['accessURL'] = ''
ecooProvDict['Library']['wasAttributedTo'] = ''


prov = {
    "_comment": "Classes and properties that are not defined in the ecoop ontology are assigned the prefix ecoop_ext. We may do one of the following things: 1) Skip collecting these pieces of information; 2) Extend the ecoop ontology to include these properties and classes; 3) Find existing properties and classes, not necessarily in the ecoop ontology, to take their places.",
    "@context":
        {
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "ecoop": "http://escience.rpi.edu/ontology/eco-op/ecoopProv.ttl#",
            "owl": "http://www.w3.org/2002/07/owl#",
            "foaf": "http://xmlns.com/foaf/0.1/",
            "skos": "http://www.w3.org/2009/08/skos-reference/skos.rdf#",
            "dctype": "http://purl.org/dc/dcmitype/",
            "prov": "http://www.w3.org/ns/prov#",
            "dct": "http://purl.org/dc/terms/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "dcat": "http://www.w3.org/ns/dcat#",
            "qudt": "http://qudt.org/1.1/schema/qudt#",
            "ex" : "http://not.sure/yet#",
            "ecoop_ext": "http://escience.rpi.edu/ontology/eco-op/ecoopProvExt.ttl#"
        },
    "@graph": [],
    }
