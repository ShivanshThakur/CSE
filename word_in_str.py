# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:39:56 2019

@author: test
"""

import re
s=input('Enter string :')
li=re.findall('\S+', s)
for i in li:
    print(i)