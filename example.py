#!/usr/bin/env python

try: import json
except: import simplejson as json
import urllib
import makechart

url = 'http://quandyfactory.com/json/makechart' # chart with world petroleum production data by month from EIA
output = urllib.urlopen(url)
contents = output.read()

dataset = json.loads(contents)
caption = 'World Oil Production by Month, 2001-2010<br>(Source: EIA)'
unit = 'mbpd'
chart = makechart.make_chart(dataset, caption, unit)
html = makechart.make_html(chart)

file = open('makechart_example.html', 'w')
file.write(html)
file.close

