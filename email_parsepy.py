# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:16:14 2019

@author: test
"""

st=input('Enter string :')
em=''
f=st.rfind('@')#finds the last occurance of substring...
l=st.rfind('.')
for i in range(f+1, l):
    em+=st[i]
print('Email server :', em)