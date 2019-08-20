# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:24:06 2019

@author: sitesh
"""

dom=''
tim=''
c=0
d=input("Enter scrapped data :")
for i in range(len(d)):
    if(d[i]=='@'):
        i+=1
        while(d[i]!='.'):
            dom+=d[i]
            i+=1
    if(d[i]==':' and c==0):
        c=1
        i-=2
        while(d[i]!=' '):
            tim+=d[i]
            i+=1
print("\nDomain :", dom)
print("Time :", tim)
        