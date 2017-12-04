

'''Doc: solution <problemset 2>
   
Question : 5 
Author: divya.natarajan@accenture.com
   
Date:

04/12/2017'''



def digit(s):
  t = 0
  for i in s:
    try:
      t = t+int(i)
    except ValueError:
      pass 
  print t
s=raw_input('Enter the String : ')
digit(s)