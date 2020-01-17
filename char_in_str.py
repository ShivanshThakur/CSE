# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:36:41 2019

@author: test
"""

import re
s=input('Enter string :')
li=re.findall('[A-Za-z0-9]', s)
print(li)