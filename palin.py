# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:07:16 2019

@author: sitesh
"""

st=input("Enter a string / number:")
if(st == st[::-1]):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")