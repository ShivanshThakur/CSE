# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:26:48 2019

@author: test
"""

n=int(input("Enter limit :"))
for i in range(0, n):
    for j in range(1, n-i):
        print('', end=' ')
    for k in range(0, i):
        print('*', end='')
    print('')