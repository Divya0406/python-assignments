'''Doc: solution <problemset 3>
Question : 2
Author: divya.natarajan@accenture.com
Date:05/12/2017'''


str=raw_input("enter the string to be rotated in lower case:")
n=int(raw_input("enter the number"))
temp=''
for i in str:
  c=ord(i)+n
  if c>=97 and c<=122:
    temp=temp[0:]+(chr(c))  
  elif c<97:
    c=c+26
    temp=temp[0:]+(chr(c))
  elif c>122:
    c=c-26
    temp=temp[0:]+(chr(c))
print(temp)