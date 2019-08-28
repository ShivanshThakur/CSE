# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:48:36 2019

@author: test
"""

di={0 : 0, 1 : 1}
l=int(input("Enter limit :"))
a=di[0]
b=di[1]
for i in range(2, l):
    s=a+b
    a=b
    b=s
    di[i]=s
print("Fibonacci dictionary :", di)

i=int(input("Enter term number :"))
if(i<=l):
    print(di[i-1])
else:
    print("Index out of range.")