'''python handson 
  Day 1
Date : 10/12/2017
Question :Write a Python program to check whether a year is leap year or not
'''  


a=int(raw_input("enter the year"))

if a%4==0:
  if a%100==0:
    if a%400==0:
      print a,"is leap year"
    else:
      print a,"is not a leap year"
  else:
    print a,"is leap year"
else:
  print a,"is not a leap year"