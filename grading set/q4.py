'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.'''


'''function to check the correctness of the password
   input : list of passwords
   output: list of valid passwords'''
def passcheck(l1):
  l2=[]
  for j in l1:
    #checking for length min 6 and max 12
    if len(j)<6 or len(j)>12:
      continue
    else:
      falpha=0
      fnum=0
      fc=0
      fsc=0
      for i in j:
        #checking for alphabets
        if i.isalpha():
          if i.isupper():
            falpha=1
          elif i.islower:
            fc=1
        #checking for numbers    
        elif i in ['1','2','3','4','5','6','7','8','9','0']:
          fnum=1
        #checking for special characters  
        elif i in ['$','#','@']:
          fsc=1
        else:
          break
          
        
      if falpha==1 and fnum==1 and fsc==1 and fc==1:
        l2.append(j)
  return ",".join(l2)
    
    

a=raw_input("enter the comma seperated passwords:")
l1=a.split(",")
c=passcheck(l1) 
print c

#test function
def test_password():
  print "\n----test_function----"
  l2=['aA#12','Vd@0419','aeiOU@1234567','abc#123','SSG@#34','Darg123','Hill#$@','1234@#$','Acc9876$$','t W*7#']
  print l2
  x=passcheck(l2)
  print"\nthe valid passwords are:" ,x

#call of test_password
test_password()
