'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.'''

#input the value eg: 3,4 
a=raw_input("enter the numeric value for m,n in comma seperated form:")
l1=a.split(',')
l2=[]
l3=[]
l5=[]
#converting the string into int
b=int(l1[0])
c=int(l1[1])
#generating the m values
for i in range(0,b):
  l2.append(i)
#generating the n values  
for i in range(0,c):
  l3.append(i)
  
#creating a 2-dimensional array  
for i in l2:
  l4=[]
  for j in l3:
    l4.append(i*j)
  l5.append(l4)
print l5  
