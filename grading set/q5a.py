'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :(a)Write a program that will ask the user for a number and then print out a list of number from 1 to the number entered and the square of the number. For example, if the user entered '3' then the program would output:

1 squared is 1. 2 squared is 4. 3 squared is 9.'''


#accepts only integer datatype
try:
  a=int(raw_input("enter the number:"))
  for i in range(1,a+1):
    print i,"squared is", i*i
    
#displays the error message when other datatypes are used    
except ValueError:
  print "Input should be integer. No other datatypes are allowed"
