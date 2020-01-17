# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:58:28 2019

@author: test
"""

count=0
s=input('Enter string :')
c=input('Enter character :')
for i in s:
    if(c==i):
        count+=1
print('Found character', count, 'time(s)')
        