  
'''python handson 
  Day 2
  Date : 10/12/2017
  Question :Declare a List containing Numbers a) Get only Even Numbers b) Perform sum of those even Numbers'''  
  
print "enter 5 numbers"
a=[]
m=0
for i in range(1,6):
  c=int(raw_input("enter the number:"))
  if c%2==0:
    a.append(c)
for i in a:
  m=m+i
print "list:",a 
print "sum of the list:",m