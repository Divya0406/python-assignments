'''Problemset : 4
Author : Divya.natarajan
Date : 09/12/2017
Question: 6'''


#abstract class
class Temperature:
  def __init__(self, temperature):
    pass
  def __str__(self):
  	pass
  def abovefreezing(self,temp):
    pass
  def convertToFahren(self):
    pass
  def convertToCelsius(self):
    pass
  def convertToKelvin(self):
    pass
  
#derived class
class Farenheit(Temperature):
  def __init__(self,t):
    self.temp=t
  def __str__(self):
    return self.temp
  def abovefreezing(self):
    if self.temp>=32:
      return "true"
    else:
      return "false"
  def convertToFahren(self):
    return self.temp
  def convertToCelsius(self):
    tocel=self.temp/33.85
    return tocel
  def convertToKelvin(self):
    tok=self.temp*255.9
    return tok

#derived class    
class Celsius(Temperature):
  def __init__(self,t):
    self.temp=t
  def __str__(self):
    return self.temp  
  def abovefreezing(self):
    if self.temp>0:
      return "true"
    else:
      return "false"
  def convertToFahren(self): 
    tofa=self.temp*33.8
    return tofa
  def convertToCelsius(self):
    return self.temp
  def convertToKelvin(self):
    tok=self.temp*274.15
    return tok    

#derived class    
class Kelvin(Temperature):
  def __init__(self,t):
    self.temp=t 
  def __str__(self):
    return self.temp
  def abovefreezing(self):
    if self.temp>=273:
      return "true"
    else:
      return "false"
  def convertToFahren(self):
    a=9/5.0
    return (self.temp*a)-459.67
  def convertToCelsius(self):
    tocel= self.temp-273.15
    return tocel
  def convertToKelvin(self):
    return self.temp
    
    
a=float(raw_input("enter the temperature:"))
f=Farenheit(a)
c=Celsius(a)
k=Kelvin(a)
print f.__str__(),"degree Farenheit"
print c.__str__(),"degree celsius"
print k.__str__(),"kelvin"
print "\nfreezing point"
print "freezing point of Farenheit? :",f.abovefreezing()
print "freezing point of celsius?:",c.abovefreezing()
print "freezing point of kelvin?:",k.abovefreezing()
print "\nconversions"
print "\n from Farenheit"
print f.convertToFahren(),"degree Farenheit"
print f.convertToCelsius(),"degree celcius"
print f.convertToKelvin(),"kelvin"
print "\n from Celsius"
print c.convertToFahren(),"degree Farenheit"
print c.convertToCelsius(),"degree celcius"
print c.convertToKelvin(),"kelvin"
print "\n from kelvin"
print k.convertToFahren(),"degree Farenheit"
print k.convertToCelsius(),"degree celcius"
print k.convertToKelvin(),"kelvin"

'''Create a list of Temperature objects of a mix of Temperature types'''
l1=
'''Print out the value of each temperature in the list, and add “above freezing” if the temperature is above freezing (for the specifi c temperature scale).'''
for i in l1:
  print i.__str__()
  print "above freezing point?", i.abovefreezing()
l2=[]
'''Create a new list of temperatures containing each temperature of the original list converted to a common temperature scale (Fahrenheit, Celsius, or Kelvin).'''
for i in l1:
  if i!=c:
    temp=i.convertToCelsius()
    l2.append(temp)
    print 
'''For each temperature object in the new list, print out its temperature value, and if it is above the freezing point.'''    
for i in l2:
  cel=Celsius(i)
  print "above freezing point?",cel.abovefreezing()

    
