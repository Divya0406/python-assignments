'''Doc: solution <problemset 3>
Question : 9
Author: divya.natarajan@accenture.com
Date:05/12/2017'''

def anagram(str1,str2):
  a=sorted(str1)
  b=sorted(str2)
  if a==b:
    print "true"
  else:
    print "false"
 
  
str1=raw_input("enter the string:")
str2=raw_input("enter the string:")
anagram(str1,str2)
