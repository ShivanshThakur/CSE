# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:38:39 2019

@author: test
"""

mylist=['a', 'hello', 4.17, 78]
list=['hello', 'go', 2.4]
print(mylist)
mylist+=['a']
print(mylist)
print(['a'])
mylist.remove(4.17)
print(mylist)
####################################
mylist.append(list)
print(mylist)
####################################
mylist.extend(list)
print(mylist)
####################################
mylist.remove(["hello", "go", 2.4])
print(mylist)
####################################
mylist.insert(2, ["hello", "world"])
print(mylist)
####################################
mylist.clear()
print(mylist)
####################################
print(list.pop(0))
print(list)
####################################
list.reverse()
print(list)
####################################
print(list.index("go"))
print(list)
####################################
list1=list.copy()
print(list1)
####################################
list1=[56,78,409,5904,34,4,12,354,5]
list1.sort(reverse=True)
print(list1)
####################################