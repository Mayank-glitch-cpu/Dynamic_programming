# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 01:07:15 2021

@author: mayank
"""

x= float(input('Enter Number'))
epsilon= 0.000001
low=0.0
high= x
num_guess=0
mid= (low+high)/2
#if x<0:
 # print('Square Root Does not Exsist')
    
while abs(mid**2 - x)>=epsilon:
    print(f'low value {low} and High Value {high}')
    num_guess+=1
    if mid**2<x :
        low=mid
    else:
        high=mid 
    mid=(low+high)/2

print(f'Number of times loop runs {num_guess}')
print(f'Square root of {x} is: {mid} ')       