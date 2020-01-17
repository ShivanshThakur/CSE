# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:20:54 2019

@author: test
"""

s=input('Enter string :')
c=input('Enter character :')
ind=0
fl=0
for i in range(len(s)):
    if(c==s[i]):
        ind=i+1
        fl=1
        break
if(fl==0):
    print(c, 'not found')
else:
    print('Found', c, 'at', ind)