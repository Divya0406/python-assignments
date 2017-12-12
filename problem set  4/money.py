'''Problemset : 4
Author : Divya.natarajan
Date : 09/12/2017
Question:Design and implement a Money class that stores monetary values in dollars and cents. Special method init should have the following function header, def init(self, dollars, cents) Include special method repr (str) for displaying values in dollars and cents: $ 0.45, $ 1.00, $ 1.25. Also include special method add, and three getter methods that each provide the monetary value in another currency. Choose any three currencies to convert to. '''

class Money:
  def __init__(self,dollars,cent):
    self.dollars=dollars
    self.cent=cent
  '''displays the dollar value
     input in the form of dollar and cent
     dollar=1, cent=54
     output dollar and cent together
     $ 1.54'''
  def repr(self):
    if int(self.cent)<=99:
      s=(self.dollars,self.cent)
      self.mvalue=float(".".join(s))
      print 'The currency is $',self.mvalue
    else:
      c=float(self.cent)/100
      self.mvalue=float(self.dollar)+c
      print 'The currency is $',self.mvalue
    self.add()  
    print "value in Rs :", self.getrs()
    print "value in euro:", self.geteuro()
    print "value in Yen:", self.getyen()
  #convertion to other currency  
  def add(self):    
    self.rs=self.mvalue*64.48
    self.euro=0.85*self.mvalue
    self.yen=self.mvalue*113.51
  #getter functions  
  def getrs(self):
    return self.rs
  def geteuro(self):
    return self.euro
  def getyen(self):
    return self.yen
    
    


#object instantiation
a=raw_input("enter the dollar:")
b=raw_input("enter the cent:")
obj=Money(a,b)
obj.repr()