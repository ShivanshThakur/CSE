# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:35:28 2019

@author: sitesh
"""

def mat(row, col):
    ma=[]
    #row=int(input("Enter number of rows :"))
    #col=int(input("Enter number of columns :"))
    for i in range(row):
        r=[]#important to continuously redefine
        #print(">>", r)
        #print("!>>>", ma)
        for j in range(col):
            print("Enter [{0}][{1}] :".format(i+1, j+1))
            r.append(int(input()))
            #print(">>", r)
            #print(">>>", ma)
        #print("!>>", r)
        ma.append(r)
        #print("!>>>", ma)
    for i in range(len(ma)):
        print(ma[i])
    return ma

def matsum(m1, m2):
    m=[]
    for i in range(len(m1)):
        r=[]
        for j in range(len(m1[0])):
            r.append(m1[i][j]+m2[i][j])
        m.append(r)
    return m 
            
r1=int(input("Enter number of rows :"))
c1=int(input("Enter number of columns :"))
m1=mat(r1, c1)

r2=int(input("Enter number of rows :"))
c2=int(input("Enter number of columns :"))
m2=mat(r2, c2)

if(c1==c2 and r1==r2):
    print("\nSum of two matrices :")
    m=matsum(m1, m2)
    for x in m:
        print(x)
else:
    print("\nAddition not possible.")