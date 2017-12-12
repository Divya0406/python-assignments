'''Problemset : 4
Author : Divya.natarajan
Date : 09/12/2017
Question:Write both a nonrecursive and recursive function that displays the rows of asterisks given below,

            **
	         ****
          ******
        **********
       ************
      **************'''

#nonrecursive function using for loop
def nonrec():
  for i in range(2,15,2):
    s='*'*i
    print s.center(15)

#recursive function    
def rec(k):
  if k==16:
    return
  s='*'*k 
  print s.center(15)
  rec(k+2)

print "output of nonrecursive function:"
nonrec()  
print "output of recursive function"
rec(2)