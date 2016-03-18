"""
File: <smoothed_Heaviside.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Program to test function.>
"""

from math import pi, sin

def H_eps(x, eps = 0.01):
  if x < -eps:
      value = 0
  if -eps <= x <= eps:
      value = 1/2 + x/2*eps + (1/2*pi)*sin(pi*x/eps)
  if x> eps:
      value = 1
  return value

def test_H_eps():
 if H_eps(-0.02)!= 0:
     print "error a"
 elif H_eps(-0.01) != 1/2 + -0.01/2*0.01 + (1/2*pi)*sin(pi*-0.01/0.01):
     print "error b"
 elif H_eps(0) != 1/2 + 0/2*0.01 + (1/2*pi)*sin(pi*0/0.01):
     print "error c"
 elif H_eps(0.02) != 1:
     print "error d"
 else:
     print "Good Job!"

test_H_eps()
