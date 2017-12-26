'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 19/12/2017
   Question   :Write a one- to three-line block of code for each of the following tasks: '''
   
   
''' Create a string with 50 exclamation points (!) using the * operator. '''
print "\nProgram to print ! 50 times"
print ('!'*50)

'''Print out even numbers from 0 to 100. '''
print "\nEven number till 100"
for i in range(0,101):
  if i%2==0:
    print i

''' Convert a user-entered number from a string to an integer. '''
print "\nChanging the input into a int datatype"
a=raw_input("enter a whole number")
print a,"is of", (type(a))
a=int(a)
print "after conversion"
print a,"is of", (type(a))

'''Determine whether a user-entered integer is odd. Come out with a Common Message "Entry Validated".(Do not display any thing for even.)'''
print "\nDisplay the odd number"
a=int(raw_input("enter a whole number"))
if a%2!=0:
  print "Entry validated"
  
'''Concatenate an empty tuple and a singleton with the += statement.'''
print "\nConcatenating the empty tuple"
t=tuple()
t1=('a',)
t+=t1
print t
print t ,"is of" ,(type(t))

'''Perform Mutable operation on a List and also append using += statement.'''
print "\nAppending list in 2 ways 1. .append() \n2. += operator"
l1=[1,2,3]
l1.append(4)
print l1
l1+=[5]
print l1
    
