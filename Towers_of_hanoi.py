# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:55:45 2021

@author: mayank
"""

def moveFrm(fr,to):
    print('Move From'+ str(fr)+'to'+str(to))
def towers(x,fr,to,spare):
    if x==1:
        moveFrm(fr,to)
    else:
        towers(x-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(x-1,spare,to,fr)