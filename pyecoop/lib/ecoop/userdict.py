#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dictionary to store users information

"""
from ecoop.groupdict import ecoopgroup


ecoopuser = {}

ecoopuser['anonymous'] = {
                "@id": "ex:anonymous",
                "@type": "foaf:Person",
                "ecoop:address": "",
                "ecoop:isMemberOf": [
                    {
                        "@id": "ex:ecoop_group",
                        "@type": "foaf:Group",
                        "foaf:name": ""
                    },
                    {
                        "@id": "ex:TWC",
                        "@type": "foaf:Organization",
                        "foaf:name": "",
                        "ecoop:subOrganizationOf":
                            {
                                "@id": "ex:",
                                "@type": "foaf:Organization",
                                "foaf:name": ""
                            }
                    }],
                "foaf:familyName": "",
                "foaf:givenName": "",
                "foaf:homepage":
                    {
                        "@id": "",
                        "@type": "foaf:Document"
                    },
                "foaf:mbox": {"@id": "mailto:"},
                "foaf:phone": {"@id": "tel:"}}

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