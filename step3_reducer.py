#!/usr/bin/env python
import sys

current_website = None
current_website_consecutive_spike = 0
current_consecutive_spike = 0
website = None
spike = 0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    line = line.strip('\n')
    website_date_spike = line.split('\t')

    # convert str values (currently a string) to int
    try:
        website = website_date_spike[0].strip()
        # Ignoring date because it is used only for sorting
        spike = int(website_date_spike[2])
    except ValueError:
        # website/date/spike is not in expected format
        print('Exception WDS:', website_date_spike)
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_website == website:
        if spike == 0:
            if current_consecutive_spike >= 2:
                current_website_consecutive_spike += (current_consecutive_spike - 1)
            # Reset the spike count
            current_consecutive_spike = 0
        else:
            current_consecutive_spike += spike
    else:
        if current_consecutive_spike >= 2:
            current_website_consecutive_spike += (current_consecutive_spike - 1)
        if current_website_consecutive_spike > 0:
            # write result to STDOUT
            print('%s\t%s' % (current_website, current_website_consecutive_spike))
        # New website - Reset spike count
        current_website = website
        current_consecutive_spike = spike
        current_website_consecutive_spike = 0

# do not forget to output the last word if needed!
if current_website:
    if current_consecutive_spike >= 2:
        current_website_consecutive_spike += (current_consecutive_spike - 1)
    if current_website_consecutive_spike > 0:
        # write result to STDOUT
        print('%s\t%s' % (current_website, current_website_consecutive_spike))