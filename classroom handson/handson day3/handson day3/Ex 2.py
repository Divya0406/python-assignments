'''python handson 
  Day 3
  Date : 12/12/2017
  Question :Create a student details dictionary having {'student1':[marks1,marks2, marks3],'student2':[marks1,marks2,marks3]}

a) Create the dictionary as mentioned above b) Need to perform total and average of the marks for each student'''
  
stud = {'student1':[78,85,100],'student2':[56,87,90]}
print(stud)
for name,marks in stud.items():
  m=0
  for i in marks:
    m=m+i
  avg= m/3;
  print "total:",m, "average:", avg  
