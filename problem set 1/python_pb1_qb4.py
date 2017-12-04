'''Doc: solution <problemset 1>
   
Question : 4
   
Author: divya.natarajan@accenture.com
   Date:04/12/2017'''
  


def sum(a,b):
  
	c=float(a)+float(b)
  
	return c

def sub(a,b):
  
	c=float(a)-float(b)
  
	return c

def mul(a,b):
  
	c=(float(a)*float(b))
  
	return c

def div(a,b):
  
	c=(float(a)/float(b))
  
	return c



#solution <4a>



r=5

p=3.14

r3=mul(mul(r,r),r)

p1=(div(4,3))

sphere=mul(mul(p1,p),r3)

print(sphere)



#solution <4b>



a=24.95

dr=sub(a,mul(div(40,100),a))

ws=sum(sum(dr,3),mul(59,0.75))

print("the wholesale rate is:%f"% ws)
