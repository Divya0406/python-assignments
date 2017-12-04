'''Doc: solution <problemset 2>
   
Question :1   
Author: divya.natarajan@accenture.com
   
Date:
04/12/2017     ''' 


def gcd(a,b):
  
  
    c=min(a,b)
  
  
    for i in range(c,1,-1):
    
    
        if a%i==0 and b%i==0:
      
      
      
            print("gcd: %d"% i)    
    
        break
  


a=int(raw_input("enter the first number:"))


b=int(raw_input("enter the second number"))


gcd(a,b)