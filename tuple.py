# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:24:11 2019

@author: test
"""


mytuple=('a', 'b', 'hello', 'c', 'e', 'f', 'g', 3.4, 7.9)
print(mytuple)
mygroup=('x', 'y', 'z', 'w')
print(mygroup)
mygroup+=mytuple
print(mytuple)
print(mytuple[0:4], " ", mygroup[1:3])#For range, can be -ve / +ve if not overlapping
print(mytuple*2)
print(mytuple)
###
print(mytuple[::2])#increment(l->R) or decrement(R->L) 
print(mytuple[2::])#starting point is determined(L->R) 
print(mytuple[-9 : 0])#Overlapping index 