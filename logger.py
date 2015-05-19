#!/usr/bin/python

import json
import uuid
import time


def get_giant_json(size):
    iter_bytes = 80
    mydict = {}
    for i in xrange(0, int(size / iter_bytes)):
        mydict[str(uuid.uuid4())] = str(uuid.uuid4())
    return json.dumps(mydict)

for kb in xrange(0, 120):
    size = kb * 1024
    print "Asking for %s bytes" % size
    data = get_giant_json(size)
    print "Outputting %s bytes next" % len(data)
    print data
    print "done outputting %s bytes" % len(data)

for i in xrange(1, 60):
    time.sleep(1)
    print "This is a short log line"
