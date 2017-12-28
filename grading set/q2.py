'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :Please write a program which counts and prints the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

>>>	a,2
	c,2
	b,2
	e,1
	d,1
	g,1
	f,1
Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.'''


def cnt(a):
  '''performing the count function of string
  eg : str=abcab
  i='a'
  str.count(i) gives theoutput 2''' 
  for i in a:
    b=a.count(i)
    dict[i]=b
  for k in dict:  
    print k,":",dict.get(k) 
  
 
def testfunc():
  print "\n----test_function----"
  print "Input string: abcdefgabc"
  cnt("abcdefgabc")
  print "Input string: abcd1234abcd"
  cnt("abcd1234abcd")
  
#getting the input string
dict={}
a=raw_input("enter the string:")
cnt(a)
testfunc()
