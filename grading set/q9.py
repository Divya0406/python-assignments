'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 19/12/2017
   Question   :Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.'''

'''input : comma seperated value
output: list of odd numbers''' 

def odd(a):
  l1=[]
  for i in a:
    if int(i)%2!=0:
      l1.append(int(i))
  print l1
  #list comprehension to calculate the square of odd number
  l2=[i**2 for i in l1]
  print l2

#test function  
def test_fun():
  print "\n----test_function----"
  l1=[1,2,3,4,5,6,7,8,9]
  print l1
  odd(l1)
  
try:  
  a=raw_input("enter the comma seperated value:")
  a=a.split(',')
  odd(a)
  

except ValueError:
  print "Enter the list of integer values"

finally:  
  test_fun()
