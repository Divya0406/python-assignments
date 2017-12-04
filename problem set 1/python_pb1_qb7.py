'''Doc: solution <problemset 1>
   
Question : 7
   
Author: divya.natarajan@accenture.com
   Date:04/12/2017'''





def isIn(str1,str2):
  
	if 1==1:
    
		a=str1.find(str2)
    
		return a
  
	else:
    
		a=str2.find(str1)
    
		return a



b=raw_input("enter the first string:")
c=raw_input("enter the second string")

d=isIn(b,c)

if d==-1:
  
	print("false")

else:  
  
	print("true")