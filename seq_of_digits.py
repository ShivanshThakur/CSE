# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:31:46 2019

@author: test
"""

import re
s=input('Enter a string :')
li=re.findall('[0-9]+\s[A-Za-z]', s)
print('Found expression(s) :')
for i in li:
    print(i)