'''Doc: solution <problemset 1>
  
 Question : 6
   
Author: divya.natarajan@accenture.com
   Date:04/12/2017'''



s=raw_input("Enter the decimal:")

s1= s.split(',')

s2=[]

for i in s1:
  
	i=float(i)
  
	s2.append(i)

m=0

for i in s2:
  
	m=m+i

print("total: %f" % m) 