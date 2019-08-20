# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:00:14 2019

@author: sitesh
"""

import math

print("1. 2D Point\n2. 3D Point\n")
c=int(input("Enter :"))
if c==1:
    x1, y1=input("Enter value of x1, y1 :").split()
    x1, y1=int(x1), int(y1)
    x2, y2=input("Enter value of x2, y2 :").split()
    x2, y2=int(x2), int(y2)
    print("Distance :", round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2))
elif c==2:
    x1, y1, z1=input("Enter value of x1, y1, z1 :").split()
    x1, y1, z1=int(x1), int(y1), int(z1)
    x2, y2, z2=input("Enter value of x2, y2, z2 :").split()
    x2, y2, z2=int(x2), int(y2), int(z2)
    print("Distance :", round(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2), 2))
else:
    print("Invalid Choice :")