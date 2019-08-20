# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 05:51:24 2019

@author: sitesh
"""

def fib(n):
    if(n<=1):
        return 0;
    else:
        return (fib(n-1)+fib(n-2));

n=int(input("Enter a number :"))
for i in range(n):
    print(fib(i))