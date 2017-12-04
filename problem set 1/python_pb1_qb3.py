'''Doc: solution <problemset 1>
   
Question :3
   
Author: divya.natarajan@accenture.com
   Date:


04/12/2017'''

l1=[]

l2=[]

for i in range(1,11):
 
	l2.append(int(raw_input("enter the 	number:")))

print(l2)

for i in l2:
  
	if i%2!=0:
    
		l1.append(i)

if len(l1)==0:
  
	print("there is no odd number")

else:
  
	m=max(l1)
  
	print("the largest odd value is %d"%m)