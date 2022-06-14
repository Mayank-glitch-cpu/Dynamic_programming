# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:12:21 2021

@author: mayank
"""

def gcdRecur(a,b):
    
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)