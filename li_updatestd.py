# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:24:47 2019

@author: sitesh
"""

n=input("Enter Name :")
r=int(input("Enter roll no. :"))
m=float(input("Enter total marks :"))
li=[["Name", "Roll No", "Marks"]]
li.append([n, r, m])

for i in range(len(li)):
    print(li[i])
    
print("Do you want to update information?(y/n)")
c=input()
if(c=='y' or c=='Y'):
    c=int(input("What to update?\n1. Name\n2. Roll No\n3. Marks\n"))
    if(c==1):
        li[1][0]=input("Enter name :")
        print("After updating\n", li[1], sep='')
    elif(c==2):
        li[1][1]=int(input("Enter roll no :"))
        print("After updating\n", li[1], sep='')
    elif(c==3):
        li[1][2]=float(input("Enter marks :"))
        print("After updating\n", li[1], sep='')
    else:
        print("Invalid choice.")
else:
    print("---END---")  