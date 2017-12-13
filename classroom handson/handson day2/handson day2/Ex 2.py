'''python handson 
  Day 2
  Date : 10/12/2017
  Question : Write a python script to validate the strong password (combination of characters alphabets and numbers,special characters in it. if not weak password) eg: Acc9876$ it is strong password abcd it is weak password'''
  
  
a=raw_input("enter the password:")
falpha=0
fnum=0
fsc=0
for i in a:
  if i.isalpha():
    falpha=1
  elif i in ['1','2','3','4','5','6','7','8','9','0']:
    fnum=1
  else:
    fsc=1
if falpha==1 and fnum==1 and fsc==1:
  print a,"is strong password"
else:
  print a,"is weak password"
