# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:10:08 2019

@author: test
"""
s=input('Enter a string :')
sc=''
for i in range(len(s)-1, -1, -1):
    sc+=s[i]
print('After reversing...',sc ,sep='\n')