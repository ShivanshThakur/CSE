# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:45:59 2019

@author: sitesh
"""

import math

def oct(n1):
    st=''
    while(1):
        r=int(n1%8)
        n1=int(n1/8)
        st+=str(r)
        if(n1==0):
            break
    print("Octal Form :", int(st[::-1]))
    
def hex(n1):
    #n1=int(input("N1 :"))
    st=''
    while(1):
        r=int(n1%16)
        n1=int(n1/16)
        if(r>=0 and r<=9):
            st+=str(r)
        else:
            switcher = {
                10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'
            }
            st+=switcher.get(r)
        #print(st)
        if(n1==0):
            break
    print("Hexadecimal Form :", st[::-1])
    
########################################################

n=input("Enter a number :")

print("Square root :", round(math.sqrt(int(n)), 2))
oct(int(n))
hex(int(n))

