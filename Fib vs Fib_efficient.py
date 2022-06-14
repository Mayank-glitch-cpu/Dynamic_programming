# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:18:41 2021

@author: mayank
"""

def fibonacci(num):
    global num_steps
    num_steps+=1
    if num==0:
      return 1
    if num==1:
        return 1
    else:
        return fibonacci(num-2)+ fibonacci(num -1)
#count= 10
#for i in range(count):
#    print(fibonacci(i), end=',')
num_steps=0
print(fibonacci(34))
print(num_steps)

def fib_eff(a,d):
    global num_steps
    num_steps+=1
    if a in d:
        return d[a]
    else:
        ans= fib_eff(a-2, d) + fib_eff(a-1, d)
        d[a]=ans
        return ans
d={1:1,2:2}  
num_steps=0  
print(fib_eff(34, d))
print(num_steps)
