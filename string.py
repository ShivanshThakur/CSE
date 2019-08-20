# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:04:29 2019

@author: test
"""

str=input("Enter a string :");
print("Character at index 0 :", str[0])
print("Before replacing, val of m :", str.count("m"))
str=str.replace("mm", "m")
print("After replacing, val of m :", str.count("m"), "\nString becomes :", str)

str1="hello, there! This is a python program"
print(str1.split(","))
print(str1.split(" "))

str2="!@#123ac"
print(max(str2))
print(min(str2))
print(str2.upper(), " ", str2.lower())