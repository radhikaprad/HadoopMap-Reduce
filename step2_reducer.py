#!/usr/bin/env python
import sys
import datetime

current_website = None
current_date = None
current_duration = 0.0
website = None
logdate = None
duration = 0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    line = line.strip('\n')
    website_date_duration = line.split('\t')

    # convert str values (currently a string) to int
    try:
        website = website_date_duration[0].strip()
        logdate = datetime.datetime.strptime(website_date_duration[1], "%Y-%m-%d")
        duration = float(website_date_duration[2])
    except ValueError:
        # website/date/spike is not in expected format
        print('Exception DD:', website_date_duration)
        continue

    spike = 0
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_website == website:
        td = logdate - current_date
        if (current_duration * 2.0) <= duration and td.days == 1: # check consecutive date
            spike = 1 # Found a spike
        else:
            spike = 0
        # write result to STDOUT
        print('%s\t%s\t%s' % (current_website, logdate.date().isoformat(), spike))
    # Update for next spike check
    current_website = website
    current_date = logdate
    current_duration = duration
