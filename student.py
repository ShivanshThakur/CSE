# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:51:50 2019

@author: test
"""

class student:
    def __init__(self, name, roll, c, year):
        self.n=name
        self.r=roll
        self.c=course(c, year)
    def disp(self):
        print('Name :', self.n)
        print('Roll No. :', self.r)
        print('Course :', self.c.get())

class dept:
    def __init__(self, name):
        self.n=name
        self.c=[]
    def get(self):
        return (self.n, self.c)
    def add(self, course):
        self.c.append(course)
    def show(self):
        print('Department name :', self.n)
        print('Courses available :', self.c)
        
class course:
    def _init__(self, name, year):
        self.n=name
        self.y=year
    def get(self):
        return (self.n, self.y)

d1=dept('CSE')
d2=dept('Physics')
d1.add('BTech')
d1.add('BCA')
d2.add('MSc')
d2.add('MA')
print('Courses in :')
d1.show()
print('\n')
d2.show()
print('\n')
ch=input('Enter course :')
y=int(input('Enter year :'))
s=student('AAA', 123, ch, y)
s.disp()