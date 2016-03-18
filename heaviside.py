"""
File: <heaviside.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Create program to test functions.>
"""
def H(x):
   if x <0:
       value =0
   if x>=0:
       value = 1
   return value

def test_H():
   if H(-10)!= 0 :
       print "error"
   elif H(10**25) !=0:
       print "error"
   elif H(-10**-15) !=0:
       print "error"
   elif H(0) !=1:
       print "error"
   elif H(10**-15) !=0:
       print "error"
   elif H(10) !=1:
       print "error"

print "great!"
