# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 00:09:02 2021

@author: mayank
"""

#import math
class complex(object):
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __str__(self):
        s1= 'real' + "+" + 'imaginary' + "i"
        return s1
    #def modulus(self):
     #   s1= math.sqrt(('real')**2+('imaginary')**2)
      #  return s1
    def conjugate(self):
        s1= "real" + "-" + "imaginary" + "i"
        return s1
complex1= complex('3','4')
print(complex1)
#print(complex1.modulus())
print(complex1.conjugate())