# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 06:00:29 2019

@author: sitesh
"""

a, b, c=input("Enter three side of triangle :").split(' ')
a, b, c=float(a), float(b), float(c)
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is :", area)