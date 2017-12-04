'''Doc: solution <problemset 1>
   
Question : 5
   
Author: divya.natarajan@accenture.com
   
Date:04/12/2017
'''   
   


s= raw_input("enter the integer:")

s=int(s)

flag=1

for i in [1,2,3,4,5,6,7,8,9,0]:
  
	for j in [1,2,3,4,5]:
    
		if s==pow(i,j):
      
			print("root: %d" %i)
      
			print("power: %d" %j)
      
			flag=0

if flag==1:
  
print("no such pair")