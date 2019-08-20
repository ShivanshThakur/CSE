# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:41:46 2019

@author: test
"""

n=int(input("Enter limit :"))
for i in range(1, n+1):
    for j in range(0, n-i):
        print('', end=' ')
    for k in range(1, i+1):
        print(k, end='')
    print('')