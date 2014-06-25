def initProv():
    prov = {"@id": "http://not.sure/yet#notebook_run",
        "@type": [
            "http://www.w3.org/ns/prov#Activity"
        ]}
    return prov

def provStartedAtTime(now):
    StartedAtTime = [{"@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                      "@value": '%s' % now
                      }]
    return StartedAtTime

def provEndedAtTime(now):
    EndedAtTime = [{"@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                    "@value": '%s' % now
                    }]
    return EndedAtTime

def provWasAssociatedWith(usernames):
    usernames = usernames.split(" ")
    WasAssociatedWith = []
    for i in usernames:
        user = {"@id": "http://tw.rpi.edu/instances/%s" % i}
        WasAssociatedWith.append(user)
    return WasAssociatedWith


def provUsed(software):
    software = software.split(" ")
    provUsed = []
    for i in software:
        sw = {"@id": "ex:%s" % i}
        WasAssociatedWith.append(sw)
    return provUsed
