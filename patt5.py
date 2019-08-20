# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:48:19 2019

@author: test
"""

n=int(input("Enter limit :"))
for i in range(0, n):
    for j in range(0, n-i):
        print(' ', end=' ')
    for k in range(1, i+2):
        print(k, end=' ')
    for l in range(1, i+1):
        print(l, end=' ')
    print('')