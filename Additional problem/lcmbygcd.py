'''Additional problem set
Question: LCM of two numbers using GCD
Date : 07/12/2017'''

#function to calculate gcd with 2 numbers as parameter
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
    
 
#functin to calculate LCM with GCD and 2 number as parameters      
def lcm(gcd,a,b):
  if gcd==0:
    return 0
  else:  
    j=(a*b)/gcd
    return j
  
 
def test_gcd_lcm():
  #combinations of input
  n=[0,0,2]
  m=[0,3,3]
  print "--------------------test function----------------------------"
  print "num 1 \t|\t num2 \t|\t GCD \t|\t LCM"
  print "--------|---------------|---------------|-------------------"
  #function calls
  for i in range(len(n)):
    for j in range(len(m)):
      if i==j:
        q=gcd(n[i],m[j])
        #print q,"is gcd"
        w=lcm(q,n[i],m[j])
        #print(w)
        print n[i],"\t|\t ",m[j],"\t|\t ",q,"\t|\t ",w
 
 
 
  
a=int(raw_input("enter the first number:"))
b=int(raw_input("enter the second number"))
gcda=gcd(a,b)
lcma=lcm(gcda,a,b)
print lcma,"is the lcm"


test_gcd_lcm()