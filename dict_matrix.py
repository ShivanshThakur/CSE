# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:55:35 2019

@author: test
"""

di={}
r=int(input("Enter number of rows :"))
c=int(input("Enter number of columns :"))

for i in range(r):
    for j in range(c):
        di[(i, j)]=int(input("Enter [{}][{}] :".format(i ,j)))

print("\nMatrix :")
for i in range(r):
    for j in range(c):
        print(di[(i, j)], end=" ")
    print()

#di.pop((0, 0))
#print(di)
    
#--------------------------------------------    
for i in range(r):
    for j in range(c):
        if(di[(i, j)]==0):
            di.pop((i, j))#Removing all zeroes from matrix
#--------------------------------------------
            
print("\nSparse matrix :")
for i in range(r):
    for j in range(c):
        if((i, j) not in di):
            print("0", end=" ")
            continue
        print(di[(i, j)], end=" ")
    print()            