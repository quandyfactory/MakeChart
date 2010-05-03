#!/usr/bin/env python

__title__ = 'MakeChart'
__version__ = 0.1
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/56/makechart"
__copyright__ = "(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
MakeChart is a simple script written in Python that takes an array and generates a bar chart.
"""

def add_sep(n, sep=','):
    """
    Adds a separator (default comma) to long numbers.
    Pilfered from here: http://snippets.dzone.com/posts/show/584
    Added logic to deal with decimals.
    """
    string = str(n).split('.') # deal with decimals
    s = string[0]
    
    if len(s) < 4: return str(n)
    
    try: decimal = '.%s' % (string[1])
    except: decimal = ''
        
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i+3])
        i+=3
    retval = sep.join(groups)[::-1]
    if n < 0:
        return '-%s' % retval
    else:
        return '%s%s' % (retval, decimal)

        

def get_highest_value(dataset, column):
    """
    Walks a data set to get the highest value
    """
    sortedset = sorted(dataset, key=lambda prod: prod[column])
    return sortedset[-1][column] # highest value

def make_ratio(highest_value, scale):
    """
    Generates a ratio of the highest value to the scale for other values.
    """
    return scale * 1.0 / int(highest_value)
    
def vertical(string):
    """
    Takes a string and makes it display vertically
    """
    return '%s<br>' % ('<br>'.join([char for char in string]))

    
def make_chart(dataset, caption, unit=''):
    """
    Makes an HTML bar chart out of a dataset.
    """
    output = []
    addline = output.append
    
    bars = []
    labels = []
    highest_value = get_highest_value(dataset, 1)
    ratio = make_ratio(highest_value, 200)
    for datum in dataset:
        
        bars.append('<td class="bar"><div style="height: %spx" title="%s: %s %s"></div></td>' % (int(int(datum[1])*ratio), datum[0], add_sep(datum[1]), unit))
        labels.append('<td>%s</td>' % (vertical(datum[0])))
    
    addline('<table class="makechart">')
    addline('<caption>%s</caption>' % (caption))
    addline('<tr class="bar">')
    addline('\n'.join(bars))
    addline('</tr>')
    addline('<tr class="label">')
    addline('\n'.join(labels))
    addline('</tr>')
    addline('</table>')
    
    return '\n'.join(output)
    
def make_css():
    """
    Generates basic CSS to display the bar chart
    """
    output = []
    addline = output.append
    output.append('table.makechart { border-collapse: collapse; border: 1px solid #ccc; font-size: 1em; }')
    output.append('table.makechart caption { font-weight: bold; font-size: 130%; text-align: center; }')
    output.append('table.makechart th, table.makechart td { border: 1px solid #ccc; padding: 0; }')
    output.append('table.makechart .bar td { height: 300px; text-align: center; vertical-align: bottom; }')
    output.append('table.makechart .bar td div { text-align: center; width: 100%; background: red; color: white; }')
    output.append('table.makechart .label td { text-align: center; vertical-align: top; padding: 1px; padding-bottom: 1em; background: #eef; color: darkblue; font-size: .8em; }')
    return '\n'.join(output)
    
def make_html(chart, css=make_css()):
    """
    Makes an HTML page.
    """
    output = []
    addline = output.append
    output.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" ')
    output.append('"http://www.w3.org/TR/html4/strict.dtd">')
    output.append('<html lang="en">')
    output.append('<head>')
    output.append('<meta name="author" content="Ryan McGreal">')
    output.append('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
    output.append('<meta http-equiv="Content-Style-Type" content="text/css">')
    output.append('<meta name="generator" content="MakeChart; url=http://quandyfactory.com/projects/56/makechart">')
    output.append('<title>Make Chart Example</title>')
    output.append('<style type="text/css">@import "/static/styles/style.css";')
    output.append(css)
    output.append('</style>')
    output.append('</head>')
    output.append('<body>')
    output.append(chart)
    output.append('</body>')
    output.append('</html>')
    return '\n'.join(output)
    
