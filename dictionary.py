# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:52:09 2019

@author: sitesh
"""

d={'Item' : 'Apple', 'Price' : 200}
print('Item bought :', d['Item'], '\nPrice :', d['Price'])

###

ind={1 : 'Aakarsh', 2 : 'Arsh', 3 : 'Ajay', 4 : 'Surjeet'}
for x in ind:
    print(ind[x])

###

print(d.key('Apple'))
print(ind.key('Arsh'))

###
    
print(d)    
d=ind
print(d)

###

#di=dict({'Hello' : 1, 'One' : 2})
#print(di)
#for x in di:
#    print(di[x])