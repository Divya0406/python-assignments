'''Doc: solution <problemset 3>
Question : 9
Author: divya.natarajan@accenture.com
Date:05/12/2017


def is_abecedarian(str1):
    str2=sorted(str1)
    if "".join(str1)=="".join(str2):
      print "true"
    else:
      print"false"
  
str=list(raw_input("enter the comma seperated string:"))
is_abecedarian(str)