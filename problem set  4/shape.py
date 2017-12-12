'''Problemset : 4
Author : Divya.natarajan
Date : 09/12/2017
Question : Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.'''



#parent class
class Shape:
  def area(self):
   print "the defalut area of shape is 0" 

#derived class    
class Square(Shape):
  def __init__(self,l):
    self.le=l
  #calculating the area  
  def area(self):
    re=self.le*self.le
    return re

'''instantiating the derived class'''    
obj=Square(5)
re1=obj.area()
print (re1)