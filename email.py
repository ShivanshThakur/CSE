# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:18:13 2019

@author: test
"""

import re
s=input('Enter a string :')
li=re.findall('\S+@\S+', s)
print('\nEmail found :')
for i in li:
    print(i)