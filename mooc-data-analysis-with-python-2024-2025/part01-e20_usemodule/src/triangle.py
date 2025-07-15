
"""
triangle.py
Module providing basic functions that calculate a right-angled triangles:
- hypotenuse(): returns the lenght of the hypotenuse
- area(): returns the area of the triangle

Version: 1.0
Author: Ait Oufkir Brahim

"""
__version__="1.0"
__author__ ="Ait Oufkir Brahim"


from math import sqrt

def hypotenuse(a, b):
  """Returns the hypotenuse length given two perpendicular sides."""
  c = sqrt(a**2 + b**2)
  return c

def area(b,h):
  """Calculate and return the area of a right-angled triangle."""
  return 0.5*b*h
