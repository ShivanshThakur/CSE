# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:41:20 2019

@author: test
"""

d1={}
d2={}
l=int(input("Enter number of values :"))
for i in range(l):
    m=int(input("Enter value[{}] (in m):".format(i+1)))
    cm=m*100
    d1[m]=cm
    cm=int(input("Enter value[{}] (in cm):".format(i+1)))
    m=cm/100
    d2[cm]=m
print("CM -> M")
print(d2)
print("M -> CM")
print(d1)