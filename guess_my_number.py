# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:15:36 2021

@author: mayank
"""

x=int( input('Enter any number between 0 to 100'))
#epsilon=0.00000000000001
low=0
high=100

while True:
   mid=int((low+high)/2)
   print(f'Is your Secret Number is {mid} ?') 
   y= input("Enter 'h' if guess is too high."
             "Enter 'l' if guess is too low."
             "Enter c to indicate I guessed correctly")
   #y= input("")
   
  # H=chr(104)
   #L=chr(108)
   #C=chr(99)
   if y=='h':
     high= mid
   elif y=='l':
     low=mid
   
   elif y=='c':
     print(f"Game Over your secret number was {mid}")
     break
   else:
     print("What you entered i can't get it") 
   if y!=x:
     print('Sorry I Did not Understand your Input')
   else:
       print('Sorry I Did not Understand your Input')
   #elif y=='c':
     #print(f"Game Over your secret number was {mid}")
     #break 
       
   