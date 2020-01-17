# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:15:46 2019

@author: test
"""

s=input("Enter a string :")
l={}
ma=0

for i in range(len(s)):
    if(s[i]==' ' or s[i]==':'):
        continue
    l[s[i]]=0
    
for i in range(len(s)):
    if(s[i]==' ' or s[i]==':'):
        continue
    l[s[i]]+=1
    if(l[s[i]]>ma):
        ma=l[s[i]]

#print(ma)
"""
for i, j in l.items():#horizontal histogram
    print(i,'[{}]'.format(j), sep='', end='  ')
    for m in range(l[i]):
        print('*', end='')
    print()
"""
print()

for i in range(ma, 0, -1):#vertical histogram
    for j in l:
        if(l[j]>=i):
            print('*', end='  ')
        else:
            print(end='   ')
    print()
for i in l:
    print('_', end='  ')
print()
for i in l:
    print(i, end='  ')
    
        