"""
File: <histogram2.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Print n and an n number of astericks side by side on an t-chart.>
"""
def histogram(pass_list):
   print " n | Data"
   print "---+----------------"
   for i in pass_list:
       string = ""
       for j in range (i):
           string = string + "*"
       print len(string), "|" , string
histogram([10, 14, 20, 14, 10])
