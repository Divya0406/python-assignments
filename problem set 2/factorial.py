'''Doc: solution <problemset 2>

Question : 3

Author: divya.natarajan@accenture.com

Date:

04/12/2017'''

def factI(n):
  
    m=1
  
    for i in range(1,n+1):
   
         m=m*i
  
    print("the factorial is %d"%m)
    


def factR(n):
  
    if n>=1:
   
        return n*(factR(n-1))
   
  


a=int(raw_input("enter the number"))

factI(a)

b=factR(a)

print("the factorial is:%d" % b)