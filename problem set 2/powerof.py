'''Doc: solution <problemset 2>
   
Question : 2
   
Author: divya.natarajan@accenture.com
   
Date:

 04/12/2017'''    



def pow(a,b):
  
    if b%a==0:
    
        if b/a==a:
      
            print("%d is power of %d"% b,a)
    
        else:
      
            pow(a,a/b)
 
    else:
    
        print("%d is not power of %d" % b,a)


a=int(raw_input("enter the number:"))

b=int(raw_input("enter the number:"))

c=min(a,b)

if c==a:
  
    pow(c,b)

else:
  
    pow(c,a)