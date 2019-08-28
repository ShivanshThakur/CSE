# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:19:01 2019

@author: test
"""

n=int(input("Enter number :"))
cp=0
cc=0
index=0
while(n!=-1):
    for i in range(2, n):
        if(n%i==0):
            cc+=1
            index=1
            break
    if(index==0):
        cp+=1;
    n=int(input("Enter number :"))
print("Number of prime integers :", cp)
print("Number of composite integers :", cc)