# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:27:50 2019

@author: test
"""

def find(s, subs):
    ind=0
    fl=0
    for i in range(len(s)):
        if(subs[0]==s[i]):
            j=1
            while(i+j<len(s) and j<len(subs) and subs[j]==s[i+j]):
                j+=1
            if(j==len(subs)):
                ind=i
                fl=1
    if(fl==0):
        return -1
    else:
        return ind+1

st=input('Enter string :')
print('Length :', len(st))
su=input('Enter substring :') 
#s, e=input('Enter range :').split()
#find(st, su, int(s), int(e))
if(find(st, su)==-1):
    print('Not found')
else:
    print('Found at index', find(st, su))          