# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:01:39 2021

@author: mayank
"""

num = int(input("Enter a number "))
if num ==1:
    print(f'{num}is not prime')
elif num==0:
    print(f'{num}is not prime')
else:
    for i in range(2,num):
        if num % i == 0:
           print(f'{num} is  not a prime number')
           break
    else:
        print(f'{num} is a prime number')    