#!/usr/bin/env python
import sys
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip('\n')
    tuplevalues = line.split('\t')
    website = tuplevalues[0].strip()
    startdatetime = datetime.datetime.strptime(tuplevalues[1].strip(), "%Y-%m-%d %H:%M:%S")
    enddatetime = datetime.datetime.strptime(tuplevalues[2].strip(), "%Y-%m-%d %H:%M:%S")
    td = enddatetime - startdatetime
    duration = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6 # Convert to seconds
    print("%s\t%s\t%s" % (website, startdatetime.date().isoformat(), duration))
