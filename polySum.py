# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 01:31:54 2021

@author: mayank
"""

import math
#from math import*
pie= math.pi
def polysum(n,s):
    area = (0.25*n*s**2)/math.tan(pie/n)
    crc= n*s
    sum= area+crc**2
    return round(sum,4)