'''Problemset : 4
Author : Divya.natarajan
Date : 09/12/2017
Question:Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class. '''  
  
#parent class      
class Person:
  def getgender(self):
    pass
    
#derived class of Person    
class Male(Person):
  def getgender(self):
    print "Male"
    
#derived class of person    
class Female(Person):
  def getgender(self):
    print "Female"


a=raw_input("enter the gender as m or f:")
if a=="m":
  # object instantiation 
  obj=Male()
  obj.getgender()
elif a=="f":
  obj=Female()
  obj.getgender() 