# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:57:20 2021

@author: mayank
"""

x= float(input('Enter Number'))
epsilon= 0.01
low=1.0
high= x
num_guess=0
mid= (low+high)/2
while abs(mid**3 - x)>=epsilon:
    print(f'low value {low} and High Value {high}')
    num_guess+=1
    if mid**3<x :
        low=mid
    else:
        high=mid 
    mid=(low+high)/2
#print(f'Number of times loop runs {num_guess}')
print(f'Cube root of {x} is: {mid} ')       