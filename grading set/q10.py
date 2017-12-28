'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 20/12/2017
   Question   :The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

Hints: We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.'''

'''function for generating the fibonacci series
input : number of values to be displayed
output: fibonacci series'''

def fibo(x):
  l1=[]
  l2=[]
  #f(n)=0 if n=0
  if x==0:
    l1.append(0)
  #f(n)=1 if n=1  
  elif x==1:
    l1.append(1)
  #generating fibonnaci series  
  elif x>1:
    l1.append(0)
    l1.append(1)
    [l1.append(l1[i-1]+l1[i-2]) for i in range(2,x)]
    #print l1
  elif x<0:
    print "enter a positive integer"
  for i in l1:
    l2.append(str(i))
  print ",".join(l2)  


#test function
def test_fibo():
  print "\n__test function__"
  print "fibonacci for 0:"
  fibo(0)
  print "fibonacci for 1:"
  fibo(1)
  print "fibonacci for 2"
  fibo(2)
  print "fibonacci for 12"
  fibo(12)
  print "fibonacci for negative value"
  fibo(-2)
 
  
a=raw_input("enter the positive integer value:")
try:
  a=int(a)
  fibo(a)

except ValueError:
  print "Enter a integer datatype"

finally:
  test_fibo()
