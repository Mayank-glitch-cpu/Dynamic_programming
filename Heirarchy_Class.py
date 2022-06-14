# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:41:28 2021

@author: mayank
"""

import random
class animals():
    def __init__(self,age,name):
        self.age=age
        self.name=[]
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,other_age):
        self.age=other_age
    def set_name(self,other_name):
        self.name=other_name
    def __str__(self):
        s1= "Animal " + str(self.name) + " is "+ str(self.age) + " years old. "
        return s1
    def settingname(self,name):
        self.name.append('name')
        return self.name
class Cat(animals):
     def speak(self):
        return "Meow"
     def __str__(self):
        return "Cat named "+str(self.name)+" of age " + str(self.age)
class rabbit(animals):
     def speak(self):
        return "Whoop"
     def __str__(self):
        return "Rabbit named "+str(self.name)+" of age " + str(self.age)
class person(animals):
      def __init__(self,name,age):
         animals.__init__(self,age)
         animals.get_name(self)
         self.friends=[]
      def get_friend(self):
          return self.friends
      def add_friend(self,fname):
          if fname not in self.friends():
             return self.friends.append(fname)
      def speak(self):
         e=random.random()
         if e>0 and e<0.25:
            return "hllo!!"
         if e>0.25 and e<0.5:
            return "I wanna Eat some stuff!!"
         if e>0.5 and e<0.75:
            return "I am feeling Sleepy"
         else:
            return "Bye!!"
      def compare(self,other_age):
         diff= self.get_age()-self.other_age.get_age()
         if self.get_age()>self.other_age.get_age():
             return str(self.name)+ " is older than "+ str(self.other_name)+ " by "+ str(diff)+ " Years."
         else:
             return str(self.name)+ " is younger than "+ str(self.other_name)+ " by "+ str(-diff)+ " Years."
      
            
     
        