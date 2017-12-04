'''Doc: solution <problemset 1>
   
Question :1
   
Author: divya.natarajan@accenture.com
   Date:
 04/12/2017  


'''


a=int(raw_input("enter the first value"))

b=int(raw_input("enter the second value"))
c=int(raw_input("enter the third value"))

l2=[a,b,c]

l1=[]

for i in l2:
  
	if i%2!=0:
    
		l1.append(i)

if len(l1)==0:
  
	print("there is no odd number")

else:
 
	m=max(l1)
  
	print("the largest odd value is %d"%m)