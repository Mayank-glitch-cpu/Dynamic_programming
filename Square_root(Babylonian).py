# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:01:49 2021

@author: mayank
"""

x= int(input('Enter'))
epsillon= 0.000001
current_approx= x/2
#steps=0
for i in range(50):
    new_approx=(current_approx+x/current_approx)/2
    #steps+=1
    print(f'In {i+1}th approximation {new_approx}')
    if abs(new_approx-current_approx)<epsillon:
        print(f'Root converges to {new_approx} in {i+1}th step')
        break
    else:
        current_approx=new_approx
if i>50:
   print(f'Root Converges to {new_approx}')