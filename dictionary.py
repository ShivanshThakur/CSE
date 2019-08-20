# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:52:09 2019

@author: sitesh
"""
'''
d={'Item' : 'Apple', 'Price' : 200}
print('Item bought :', d['Item'], '\nPrice :', d['Price'])

###

ind={1 : 'Aakarsh', 2 : 'Arsh', 3 : 'Ajay', 4 : 'Surjeet'}
for x in ind:
    print(ind[x])

###

print(">", d.keys())#doesn't have key 
print(">", ind.keys())#doesn't have key

###
    
print(d)    
d=ind
print(d)

###

di=dict({'Hello' : 1, 'One' : 2})
print(di)
for x in di:
    print(di[x])
    
###
'''

seq={1, 2, 3, 4, 5}
val=['Integer']
abc=dict.fromkeys(seq, val)#extra-programiz, if value appended not to be shown
print(abc)

val.append("Positive")
print(abc)



###

print(abc.get(4))
print(abc.items())
print(abc.keys())
del abc[5]
print(abc.pop(5, None))
#abc.pop_items()
print(">", abc)
print(abc.values())
abc.update({5.0 : 'Real Number', 6.7 : 'Real Number'})
print(abc)

###

for x in abc:
    print(x, ": ", abc[x], "\n")

for x, y in abc.items():
    print(x, " ", y)
    
print("\n")
    
abc[5.0], abc[6.0]=['Real Number', 'Positive'], ['Real Number', 'Positive']
del abc[6.7]

for x, y in abc.items():
    print(x, " ", y)

del abc