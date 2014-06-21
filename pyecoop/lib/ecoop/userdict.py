#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dictionary to store users information

"""
from ecoop.groupdict import ecoopgroup


ecoopuser = {}
"""
ecoopuser['epinux'] = {}
ecoopuser['epinux']['Organization'] = 'Rensselaer Polytechnic Institute'
ecoopuser['epinux']['subOrganization'] = 'Tetherless World Constellation'
ecoopuser['epinux']['Group'] = ecoopgroup['TWC']
ecoopuser['epinux']['homepageURL'] = 'http://tw.rpi.edu/web/person/MassimoDiStefano'
ecoopuser['epinux']['mbox'] = 'distem@rpi.edu'
ecoopuser['epinux']['address'] = '22 Millfield St Woods Hole MA US'
ecoopuser['epinux']['phone'] = '0015082924078'
ecoopuser['epinux']['givenName'] = 'Massimo'
ecoopuser['epinux']['familyName'] = 'Di Stefano'
"""

ecoopuser['epinux'] = {
                "@id": "ex:epinux",
                "@type": "foaf:Person",
                "ecoop:address": "22 Millfield St Woods Hole MA US",
                "ecoop:isMemberOf": [
                    {
                        "@id": "ex:ecoop_group",
                        "@type": "foaf:Group",
                        "foaf:name": "ECOOP"
                    },
                    {
                        "@id": "ex:TWC",
                        "@type": "foaf:Organization",
                        "foaf:name": "Tetherless World Constellation",
                        "ecoop:subOrganizationOf":
                            {
                                "@id": "ex:RPI",
                                "@type": "foaf:Organization",
                                "foaf:name": "Rensselaer Polytechnic Institute"
                            }
                    }],
                "foaf:familyName": "Di Stefano",
                "foaf:givenName": "Massimo",
                "foaf:homepage":
                    {
                        "@id": "http://tw.rpi.edu/web/person/MassimoDiStefano",
                        "@type": "foaf:Document"
                    },
                "foaf:mbox": {"@id": "mailto:distem@rpi.edu"},
                "foaf:phone": {"@id": "tel:+1.508.292.40780"}}

ecoopuser['JHare'] = {
                "@id": "ex:JHare",
                "@type": "foaf:Person",
                "ecoop:address": "Rhode Island",
                "ecoop:isMemberOf": [
                    {
                        "@id": "ex:ecosystem_monitoring_group",
                        "@type": "foaf:Group",
                        "foaf:name": "Ecosystem Monitoring Group"
                    },
                    {
                        "@id": "ex:NOAA_NEFSC",
                        "@type": "foaf:Organization",
                        "foaf:name": "NOAA NEFSC",
                        "ecoop:subOrganizationOf":
                            {
                                "@id": "ex:NOAA",
                                "@type": "foaf:Organization",
                                "foaf:name": "NOAA"
                            }
                    }],
                "foaf:familyName": "Hare",
                "foaf:givenName": "Jon",
                "foaf:homepage":
                    {
                        "@id": " ",
                        "@type": "foaf:Document"
                    },
                "foaf:mbox": {"@id": "mailto: @ "},
                "foaf:phone": {"@id": "tel: "}}