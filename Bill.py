# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:06:24 2019

@author: sitesh
"""

price=float(input("Enter price of book :"))
nos=int(input("Enter number of copies required :"))
dprice=price-price*(40/100)
bill=nos*dprice+3+(nos-1)*0.75
print("MRP :", price, "\nNo. of copies :", nos, "\nDiscounted Price(40% off) :", dprice, "\nDelivery charges : $3 / $0.75\n")
print("Total Price :", bill)