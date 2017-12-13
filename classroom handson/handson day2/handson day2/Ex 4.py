'''python handson 
  Day 2
  Date : 10/12/2017

  Question :Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.'''
  
a=raw_input("enter the comma seperated vaues:")
l1=a.split(',')
print l1
t1=tuple(l1)
print t1