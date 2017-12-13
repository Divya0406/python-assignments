  
'''python handson 
  
  Day 1

  Date : 10/12/2017

  Question :Calculating your birth number in numerology 26/11/1978 2+6+1+1+1+7+8 = 8'''



def add(b):

  m=0

  for i in b:

    if i.isdigit():

      c=int(i)

      m=m+c

  r=m%10

  q=m/10

  return r+q




a=raw_input("enter your birthdate:")

result=add(a)

print result