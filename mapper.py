#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip('\n')
    tuplevalues = line.split('\t')
    # Ignoring tuplevalues[0]
    department = tuplevalues[1].strip()
    yearanddate = tuplevalues[2].strip().split("-")
    year = yearanddate[0]
    sales = tuplevalues[3]
    print("%s\t%s\t%s" % (department,year,sales))
