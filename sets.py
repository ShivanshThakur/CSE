# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:15:25 2019

@author: sitesh
"""

st1={1, "hello", 3, 4.5}
print(st1)
st2={3, 4, "BYE", 5.5}
print(st2)
st3={3, 4 ,5 ,6 ,7}
'''
for x in st1:
    print(x)

st3=st1
print(st3)

print(st1 | st2)
print(st1 & st2)

st1.add("hell")
#st1.add(st2)
'''

st1.update({'abc', 'xyz', 4.5}, {'hey'}, {'he'}, "hello")
print(st1)

'''
print(len(st1))

st1.remove('abc')
st1.discard('xyz')
print(st1)

st1.clear()
#st1.remove('a')
st1.discard('a')
del st1

st1=set({'abc', 'hello', 4.5, 6.7})
print(st1)

print(st1.pop())
'''
##########################################################

#st1=st2.copy()
print(st1, st2)
###
print(st1.difference(st2))
print(st1)
print(st2.difference(st1))
###
#st1.difference_update(st2)
#print(">", st1)
###
st4=(st1.intersection(st2))
print(st1, st4)
###
st1.intersection_update(st2)
print(st4, st1)
###
print(st1.isdisjoint(st2))#are st1 and st2 disjoint sets
print(st2.issubset(st1))#is st2 subset of st1
print(st2.issuperset(st1))#is st2 superset of st1
###
st4=st1.symmetric_difference(st2)
print(">", st1.symmetric_difference(st2))
print(st4)
st1.symmetric_difference_update(st2)
print(st1)
###
print(st1.union(st2, st3))
print(st1)