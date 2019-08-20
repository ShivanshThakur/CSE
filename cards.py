# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:34:00 2019

@author: sitesh
"""

import random

c=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(c)

for i in range(12):
    r=random.randint(0, 12)
    t=c[i]
    c[i]=c[r]
    c[r]=t

print(c)