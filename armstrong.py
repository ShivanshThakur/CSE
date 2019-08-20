# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:20:23 2019

@author: sitesh
"""

def arms(n):
    s=0
    n1=n
    while(1):
        r=int(n1%10)
        s+=pow(r, 3)
        n1/=10
        if(n1==0):
            break
    if(s==n):
        print('Armstrong number')
    else:
        print('Not an armstrong number')
        
n1=int(input("Enter a number :"))
arms(n1)