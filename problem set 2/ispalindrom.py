
'''Doc: solution <problemset 2>
   
Question : 7  
Author: divya.natarajan@accenture.com
   
Date:

 04/12/2017'''


n=raw_input('enter the string')
l=[]
for i in n:
  if i.isalpha():
    j=i.lower()
    l.append(j)
str1="".join(l)
str2=str1[::-1]
if str1==str2:
  print 'palindrome'
else:
  print 'not a palindrome'