# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:25:47 2019

@author: test
"""

class student:
    def __init__(self, r, n, m):
        self.roll=r
        self.name=n
        self.marks=m
        
    def disp(self):
        print('Roll number :', self.roll)
        print('Name :', self.name)
        print('Marks :', self.marks)

s1=student(123, 'qwerty', 34.5)
s1.disp()
