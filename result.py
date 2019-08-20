# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:34:54 2019

@author: sitesh
"""

e1, e2=input("Enter marks of two subjects :").split()
e1, e2=float(e1), float(e2)
s1=float(input("Enter marks of sports event :"))
a1, a2, a3=input("Enter marks of three activities :").split()
a1, a2, a3 =float(a1), float(a2), float(a3)
res=0.5*(e1+e2) + 0.3*(a1+a2+a3) + 0.2*s1;
print("Result :", round(res), '/ 210')