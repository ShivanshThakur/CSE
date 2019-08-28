# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:16:02 2019

@author: sitesh
"""

def fibsum(n):
    li=[0, 1]
    a=0
    b=1
    s=0
    for i in range(n):
        t=a+b
        a=b
        b=t
        li.append(t)
    print(">>", li)
    for i in range(len(li)):
        if(i%2==0):
            s+=li[i]
    print("Sum :", s)

n=int(input("Enter limit :"))
fibsum(n)        