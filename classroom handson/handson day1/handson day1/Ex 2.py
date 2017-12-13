'''python handson
 
  Day 1

  Date : 10/12/2017

  Question :Get ur full name, age as input from user and print first name and last name , age using string slicing a) 2 raw_input get name and age b) print first name and last name and age c) WHEN age >= 18 , he/she is eligible to vote d) WHEN age < 18 , he/she is not eligible to vote'''


a=raw_input("enter your full name:")

b=int(raw_input("enter your age:"))

c=a.index(" ")

print "First name:",a[:c]

print "last name:",a[c+1:]

print "age :", b

if b<18:

  print "not eligible for voting"

else:

  print "eligible for voting"