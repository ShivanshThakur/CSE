# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:21:43 2019

@author: test
"""
class bill:
    d={'100':200, '101':349, '102':250, '103':150, '104':500}

    def menu(self):
        print('CODE\tPRICE')
        for i, j in self.d.items():
            print('   ', i, '\t', j, sep='')
    
    def get(self):
        self.t=0
        self.l=[]
        print('Enter quantity for each item :')
        for i in range(5):
            v=int(input(''))
            self.l.append(v)
    
    def cal(self):
        print('---BILL---')
        print('CODE \t PRICE \t QUANTITY \t ')
        for i in range(5):
            