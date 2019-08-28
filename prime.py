# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:50:15 2019

@author: test
"""

i=s=p=c=0
count=0
while(1):
    i=int(input("Enter a number (-1 to exit):") 
    if i==-1 :
        break
    for j in range(2, i):
        if (i%j==0):
            count=0
            c+=1
            break
        else:
            count=1
    if (count==1):
          p++;
print("\nTotal prime numbers :", p)
print("Total composite numbers :", c)       