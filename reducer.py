#!/usr/bin/env python
import sys

current_dept = 0
current_year = 0
current_sales = 0.0
dept = 0
year = 0
sales = 0.0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    line = line.strip('\n')
    dept_year_sales= line.split('\t')

    # convert str values (currently a string) to int
    try:
        dept = int(dept_year_sales[0])
        year = int(dept_year_sales[1])
        sales = float(dept_year_sales[2])
    except ValueError:
        # dept/year/count is not in expected format
        #print('Exception DYS:', dept_year_sales)
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_dept == dept and current_year == year:
        current_sales += sales
    else:
        if current_sales > 25000000:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_dept, current_year, current_sales))
        # Fresh start for new/next dept-year combo
        current_dept = dept
        current_year = year
        current_sales = sales

# do not forget to output the last word if needed!
if current_dept == dept and current_year == year and current_sales > 25000000:
    print('%s\t%s\t%s' % (current_dept, current_year, current_sales))
