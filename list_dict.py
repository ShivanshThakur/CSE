# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:21:26 2019

@author: test
"""

li=[]
di={}
n=int(input("Enter number of elements :"))

for i in range(n):
    li.append(input("E[{}] :".format(i)))
print("List :", li)

for i in range(n):
    di[i]=li[i]
print("Dictionary :", di)