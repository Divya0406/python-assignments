'''Doc: solution <problemset 1>
   
Question : 8
   
Author: divya.natarajan@accenture.com
   Date:04/12/2017'''  
  


def getRatios(vect1, vect2):
  
    l3=[]
  
    for index in range(len(vect1)):
    
        for index1 in range(len(vect2)):
      
            if index==index1:
        					                c=float(vect1[index])/float(vect2[index1])
        			                l3.append(c)
  
    print l3    
  



l1=raw_input("enter the first list")
l2=raw_input("enter the second list")
l1=l1.split(',')

l2=l2.split(',')

l4=[]

l5=[]

for i in l1:
  
    i=int(i)
  
    l4.append(i)

for j in l2:
  
    j=int(j)
  
    l5.append(j)

getRatios(l4,l5)