'''Doc: solution <problemset 3>
Question : Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.
Author: divya.natarajan@accenture.com
Date:05/12/2017'''

def avoids(str1,fb):
  for i in fb:
    if i in str1:
      return 0
    else:
      return 1


str=raw_input("enter the string:")
fb=raw_input("enter the forbidden letters:")
fb=fb.split(',')
re=avoids(str,fb)
if re==1:
  print "true"
else:
  print "false"