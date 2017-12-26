'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 20/12/2017
   Question   :Create a file with the following matrix X: 1 2 3 4 Read and then compute Y = 2 * X.

Read another file with a Matrix Z: 1 2 4 4 Read and then Compute(Matrix Mutilication) Y = X * Z'''

#opening the file f1.txt and write the content "1,2,3,4" into it
f1=open("f1.txt","w")
f1.write("1,2,3,4")
f1.close

#opening the file f1.txt and reading the content
f1=open("f1.txt","r")
l=f1.readline()
l=l.split(",")
l1=[]

#performing the action y=x*2
for i in l:
  i=int(i)*2
  l1.append(i)
  
#printing the result  
print "x =",l,"\ny=x*2" 
print "hence y=",l1

#opening a file f2.txt and writing content "1,2,4,4" into it
f2=open("f2.txt","w")
f2.write("1,2,4,4")
f2.close

#opening the file in read mode to read the content of the file
f2=open("f2.txt","r")
m=f2.readline()
m=m.split(",")
l2=[]

#performing the opertion y=z*x
for i in range(len(l)):
  for j in range(len(m)):
    if i==j:
      q=int(l[i])*int(m[j])
      l2.append(q)
      break

#printing the output    
print "Z=",m,"\ny=x*z"
print "hence y=",l2 
