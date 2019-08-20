# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:28:54 2019

@author: sitesh
"""

s=input("Enter string :")
c=input("Enter character :")
count=0
for i in range(len(s)):
    if(c==s[i]):
        count+=1
print("Found", count, "time(s)")