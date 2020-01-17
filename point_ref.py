# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:14:10 2019

@author: test
"""

class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def get(self):
        self.x=int(input('Enter x coordinate :'))
        self.y=int(input('Enter y coordinate :'))
        print(' ')
    def disp(self):
        print('Co-ordinates : (', self.x,', ', self.y, ')', sep='')

class location:
    def __init__(self, x, y):
        self.p=point(x, y)
    def get(self):
        self.p.x=int(input('Enter x coordinate :'))
        self.p.y=int(input('Enter y coordinate :'))
    def disp(self):
        self.p.disp()
    def ref_x(self):
        self.p.y=-self.p.y
        print('After reflecting through x axis...')
        self.p.disp()

L=location(-4, 5)
L.get()
L.disp()
L.ref_x()        