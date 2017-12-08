'''Additional problem set
Question: GCD and LCM of list of numbers
Date : 08/12/2017'''


def GCD(a,b):
  c=min(a,b)
  for i in range(c,0,-1):
    if a%i==0 and b%i==0:
      return i
      break
        
def lcm(x,b):
  m=1
  for i in b:
    m=m*i
  re=m/x
  return re

a=(raw_input("enter the comma seperated list of numbers"))
a=a.split(',')
b=[]
for i in a:
  b.append(int(i))
c=reduce(GCD, b)
print "gcd",c
lcma=lcm(c,b)
print "lcm",lcma
