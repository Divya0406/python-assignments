'''Additional problem set
Question: palindrome
Date : 08/12/2017'''


#funciton to check palindrome
def palindrome(a):
  length=len(a)
  l=length-1
  i=0 
  while(1):
    #checking for index bound
    if i==length-1 and l==0:
      break
    #execution for palindrome
    if a[i]==a[l]:
      i+=1
      l-=1
    else:
      return 0
      break
  return 1  
  
  
a=raw_input("enter the string")
if palindrome(a):
  print "palindrome"
else:
  print "not palindrome"
  
  
  
def test_palindrome():
  str1=['a','rr','noob','madam','1','1441','5467']
  print "----------test function------------"
  print "string \t|\tresult"
  for i in str1:
    if palindrome(i):
      re= "palindrome"
    else:
      re="not palindrome"
    print i,"\t\t",re

test_palindrome() 
