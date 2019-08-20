# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:05:21 2019

@author: sitesh
"""

seq={1, 2, 3, 4, 5}
val=['Integer']
abc=dict.fromkeys(seq, val)
print(abc)
###
print(abc.get(4))
###
print(abc.items())
###
print(abc.keys())
###
del abc[5]
###
print(abc.pop(5, None))
print(">", abc)
###
print(abc.values())
###
abc.update({5.0 : 'Real Number', 6.7 : 'Real Number'})
print(abc)
###