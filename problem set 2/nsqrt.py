import math


def newton_sqrt(a,x):
  
    cal=(x+a/x)/2
  
    return cal
  


def test_square_root(a,x):
  
    os=math.sqrt(a)
  
    diff=x-os
  
    print("%.1f \t|\t %.5f \t|\t %.5f \t|\t %.5f" % (a,x,os,diff))
 


b=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]

es=1.0

l1=[]

for i in b:
  
    re=newton_sqrt(i,es)
  
    if re==es:
    
        es=es+1
  
    l1.append(re)

print "Number \t|\t Newtonsqrt \t|\t math.sqr \t|\t Difference"

print "--------|-----------------------|-----------------------|---------------------" 

for i in range(len(b)):
  
    for j in range(len(l1)):
    
        if i==j:
      
            test_square_root(b[i],l1[j])