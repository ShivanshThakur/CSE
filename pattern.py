# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:04:22 2019

@author: test
"""

l=int(input('Enter limit :'))
for i in range(l):
    for j in range(i+1):
        print(chr(j+65), end=' ')
    print()