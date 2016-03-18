"""
File: <histogram.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Given n, print n amount of astericks.>
"""
def histogram(pass_list):
   for i in pass_list:
       string = ""
       for j in range (i):
           string = string + "*"
       print string
histogram([3,6,3,6,3])
