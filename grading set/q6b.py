'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 19/12/2017
   Question   : Write a function greatestCommonDivisor that takes two positive integers and computes their greatest common divisor Suppose the following input is supplied to the program: 2,30 Then, the output should be: The greatest common divisor is 2 Take the input from the user via console.'''
   
def gcd(a,b):
  #to find the denominator range
  c=min(a,b)
  #GCD(a,0)=a
  if c==0:
    if a==0:
      return b
    if b==0:
     return a
  else:
    #calculating GCD  
    for i in range(c,0,-1):
      if a%i==0 and b%i==0:
        return i
        break
    
 
 def test_gcd():
  #combinations of input
  n=[0,0,2]
  m=[0,3,3]
  print "--------------------test function----------------------------"
  print "num 1 \t|\t num2 \t|\t GCD "
  print "--------|---------------|---------------|-------------------"
  #function calls
  for i in range(len(n)):
    for j in range(len(m)):
      if i==j:
        q=gcd(n[i],m[j])
        print n[i],"\t|\t ",m[j],"\t|\t ",q, "
 
 
 
a=int(raw_input("enter the first number:"))
b=int(raw_input("enter the second number"))
re=gcd(a,b)
print re,"is the gcd"

#call of test function
test_gcd()
