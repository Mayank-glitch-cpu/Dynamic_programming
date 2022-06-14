# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:13:00 2021

@author: mayank
"""

#Decimal To Binary Converter
num= int(input('Enter Number'))
def dec_bin(num):
    if num<0:
        True
        isNeg=abs(num)
    else:
        False
    result=''
    if num==0:
        result='0'
    while num>0:
        result= str(num%2)+ result
        num= num//2
    while num<0:
        result= '-' + result
    print(f'{result}')
