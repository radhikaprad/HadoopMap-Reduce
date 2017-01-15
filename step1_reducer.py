#!/usr/bin/env python
import sys
import datetime

current_website = None
current_date = None
current_duration = 0
website = None
date = None
duration = 0
website_log_count = 0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    line = line.strip('\n')
    website_date_duration = line.split('\t')

    # convert str values (currently a string) to int
    try:
        website = website_date_duration[0].strip()
        date = datetime.datetime.strptime(website_date_duration[1], "%Y-%m-%d")
        duration = int(website_date_duration[2])
    except ValueError:
        # website/date/duration is not in expected format
        print('Exception WDD:', website_date_duration)
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_website == website and current_date == date:
        current_duration += duration
        website_log_count += 1
    else:
        if current_website:
            # write result to STDOUT
            average_duration = current_duration / website_log_count
            print('%s\t%s\t%f' % (current_website, current_date.date().isoformat(), average_duration))
        # Fresh start for new/next dept-year combo
        current_website = website
        current_date = date
        current_duration = duration
        website_log_count = 1

# do not forget to output the last word if needed!
if current_website == website and current_date == date and current_date:
    print('%s\t%s\t%s' % (current_website, current_date.date().isoformat(), current_duration))
