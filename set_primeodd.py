# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:20:53 2019

@author: test
"""

def prime(n):
    c=1
    for i in range(2, n):
        if(n%i==0):
            c=0
            break
    if(c==1):
        return n
    else:
        return 0

l=int(input("Enter limit :"))
s1, s2=set(), set()
for i in range(1, l+1):
    if(i%2!=0):
        s1.add(i)
    if(i!=1):
        x=prime(i)
        if(x!=0):
            s2.add(x)

print(s1, s2)
print("Union :", s1|s2)
print("Intersection :", s1 & s2)
print("Difference {0} and {1} :".format(s1, s2), s1.difference(s2))        
print("Difference {1} and {0} :".format(s1, s2), s2.difference(s1))
print("Symmetric difference :", s1.symmetric_difference(s2))        