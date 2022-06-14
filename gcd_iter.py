# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:59:32 2021

@author: mayank
"""

def gcd_iter(a,b):
    x= a
    #no_of_steps=0
    if a>b:
        x=b
    while  x>1:
        #print(f"Trying with {x}")
        if a%x==0 and b%x==0:
          return x
        else:
            x-=1
            #no_of_steps+=1
    return 1
#print(gcd_iter(9,12))
#print('no. of steps executed'+ str(no_of_steps))
        