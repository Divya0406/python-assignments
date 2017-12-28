'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 28/12/2017
   Question   :Write a Python program named Indiastates.py that declares a variable states with value "Maharashtra Assam TamilNadu MadhyaPradesh Karnataka".
Write a program that does the following: a) Search for a word in variable states that ends in esh. Store this word in element 0 of a list named statesList. b) Search for a word in states that begins with t and ends in u. Perform a case-insensitive comparison. [Note: Passing re.I as a second parameter to method compile performs a case-insensitive comparison.] Store this word in element 1 of statesList. c) Search for a word in states that begins with M and ends in a. Store this word in element 2 of the list. d) Search for a word in states that ends in a. Store this word in element 3 of the list. e) Search for a word that begins with M in states at the beginning of the string. Store this word at element 4 of the list. f) Output the array statesList to the screen.
Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Use list enumeration for sorting where necessary.'''


'''function to find the state ending with "esh"
 input : list of states
 output: string ending with "esh"'''
 
import re

def esh(a):
  l1=[]
  for i in a:
    a=re.compile("ESH",re.I)
    b=a.search(i)
    if b:
      l1.append(i)
  return l1

'''function to find the state starting "t" ending with "u"
 input : list of states
 output: string starting "t" ending with "u"'''  
def tn(a): 
  l2=[]
  for i in a:
    c=re.compile("t",re.I)
    d=re.compile("u$",re.I)
    e=c.match(i)
    f=d.search(i)
    if e and f:
      l2.append(i)
  return l2
  
'''function to find the state starting "M" ending with "A"
 input : list of states
 output: string starting "m" ending with "a"'''    
def ma(a):
  l3=[]
  for i in a:
    c=re.compile("m",re.I)
    d=re.compile("a$",re.I)
    e=c.match(i)
    f=d.search(i)
    if e and f:
      l3.append(i)
  return l3
  
'''function to find the state ending with "a"
 input : list of states
 output: string ending with "a"'''
def a(a):
  l4=[]
  for i in a:
    d=re.compile("a$",re.I)
    f=d.search(i)
    if f:
      l4.append(i)
  return l4
  
'''function to find the state starting with "m"
 input : list of states
 output: string starting with "m"'''
def m(a):
  l5=[]
  for i in a:
    d=re.compile("m",re.I)
    e=d.match(i)
    if e:
      l5.append(i) 
  return l5
      
      
      
state="Maharashtra Assam TamilNadu MadhyaPradesh Karnataka"
state=state.split(" ")
l2=[]

#assigning to certain index
l2.append(esh(state))
l2.append(tn(state))
l2.append(ma(state))
l2.append(a(state))
l2.append(m(state))
print l2

