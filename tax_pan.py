# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:45:58 2019

@author: sitesh
"""

def check(n, p):
    c=0
    di={'AAA' : 111, 'BBB' : 222, 'ÇCC' : 333, 'DDD' : 444, 'EEE' : 555}
    for i in di:
        if(n==i and p==di[n]):
            print("\nVerified")
            print("Tax - 7.89%")
            c=1
    if(c==0):
        print("\nCouldnt find record :", p)

n=input("Enter name :")
p=int(input("Enter PAN_ID :"))
check(n ,p)
            