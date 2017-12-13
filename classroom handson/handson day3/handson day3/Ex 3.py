'''python handson 
  Day 3
  Date : 12/12/2017
  Question :Write the below contents to a file named 'marks.txt' using python script

Science = 50 Maths = 90 English = 85 Tamil = 92

a) Read the file and calculate the total sum of marks available there'''

obj = open('marks.txt','w')
obj.write("science = 50\nmaths = 90\nenglish = 85\ntamil = 92")
obj.close()

obj=open('marks.txt',"r")
data_list= obj.readlines()
print(data_list)
temp=0
for i in data_list:
  str_list=i.split('=')
  print str_list
  no=str_list[1].strip().strip('\n')
  temp=temp+int(no)
print "total:",temp
obj.close()

