'''python handson 
  Day 1
  
Date : 10/12/2017
  
Question :Write a Python program to perform sum of three given integers. However, if any of the twovalues are equal then sum will be zero (eg : 2+1+1 = 0)
  '''


a=int(raw_input("enter the first int:"))

b=int(raw_input("enter the second int:"))

c=int(raw_input("enter the third int:"))

if a==b or b==c or c==a:

  print "sum: 0"

else:

  print "sum:",a+b+c