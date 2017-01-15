#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip('\n')
    tuplevalues = line.split('\t')
    website = tuplevalues[0].strip()
    startdate = tuplevalues[1].strip()
    spike = tuplevalues[2].strip()
    print("%s\t%s\t%s" % (website, startdate, spike))
