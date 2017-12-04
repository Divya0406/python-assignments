'''Doc: solution <problemset 1>
   
Question :2
   
Author: divya.natarajan@accenture.com
   Date:
04/12/2017     ''' 


def right_justify(s):
  
	print(s)
  
	g=s.rjust(70,' ')
  
	print(g)

s=raw_input("enter the string:")

right_justify(s)




def right_justify(s):
  
	l=len(s)
  
	g = ' '
  
	g=g*70
  
	a=g[:(70-l)]+s
 
  
	print(a)

s= raw_input("enter the string")

right_justify(s)