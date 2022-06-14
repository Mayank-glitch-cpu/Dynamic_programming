# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:34:51 2021

@author: mayank
"""

def fibonacci(num):
    if num==0:
      return 1
    if num==1:
        return 1
    else:
        return fibonacci(num-2)+ fibonacci(num -1)
count= 10
for i in range(count):
    print(fibonacci(i), end=',')
