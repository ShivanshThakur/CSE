# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:36:04 2019

@author: sitesh
"""

from datetime import date
from datetime import time
from datetime import datetime

t=date.today()
print(type(t))
print('Today is', t)
print(t.day, '/', t.month, '/', t.year)
print(t.weekday())#0-Monday, 1-Tuesday, ...

####

t=datetime.now()
print(t)
print(datetime.time(t))
print(datetime.date(datetime.now()))
#
wd=date.weekday(datetime.now())
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("Today's day number is :%d" %(wd+1))
print("Which is :", days[wd])
#

print(t.strftime("%Y"))
print(t.strftime("%a %A\n%b %B\n%d %D\n%y %Y"))
print(">>", t.strftime("%x %X"))