# coding:utf-8

import sys
from squawk.query import *
from squawk.parsers.csvparser import *
import re

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = ''

query = Query("SELECT Name,Phone FROM file WHERE Name LIKE '%%%s%%'" % name)
source = CSVParser("addressbook.csv")

for row in query(source):
        #print row
	print '%s => %s' % (row['name'], row['phone'])
