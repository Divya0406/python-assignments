'''Doc: solution <problemset 3>
Question : 7
Author: divya.natarajan@accenture.com
Date:05/12/2017'''


def using_only(str1,fb):
  for i in fb:
    if i in str1:
      return 1
    else:
      return 0


str=raw_input("enter the string:")
fb=raw_input("enter the letters as comma seperated:")
fb=fb.split(',')
re=using_only(str,fb)
if re==1:
  print "true"
else:
  print "false"
