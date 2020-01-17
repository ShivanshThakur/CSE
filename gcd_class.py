# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:38:35 2019

@author: test
"""

class fraction:
    def get(self):
        self.n=int(input('Enter numerator :'))
        self.d=int(input('Enter denominator :'))
        if(self.d==0):
            print('Division by zero not possible.')
            exit()
    
    def disp(self):
        self.__cal()
        print('After simplifying...')
        print(round(self.n), '/', round(self.d), sep='')
    
    def __cal(self):
        comm=self.__gcd(self.n, self.d)
        self.n/=comm
        self.d/=comm
    
    def __gcd(self, a, b):
        if(b==0):
            return a
        else:
            return self.__gcd(b, a%b)

f=fraction()
f.get()
f.disp()