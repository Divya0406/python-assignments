'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :(b) Alter the program to perform the following With a given integral number n, change the program to generate a dictionary that contains (i, cube of i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 7 Then, the output should be: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 373} Take the input from the user via console.'''


#accepts only integer datatype
try:
  dict={}
  a=int(raw_input("enter the number:"))
  for i in range(1,a+1):
    dict[i]= i*i*i
  print dict  
#displays the error message when other datatypes are used    
except ValueError:
  print "Input should be integer. No other datatypes are allowed"
