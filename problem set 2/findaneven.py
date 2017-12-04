
'''Doc: solution <problemset 2>
   
Question : 6   
Author: divya.natarajan@accenture.com
   
Date:

04/12/2017 '''


def f_even(l):
  for i in l:
    if i%2 == 0:
      return i
s=raw_input('Enter the list of numbers : ')
l=[]
for i in s:
  try:
    l.append(int(i))
  except ValueError:
    pass
if f_even(l):
  print 'the first even is',f_even(l)
else:
  raise ValueError('No even numbers found')