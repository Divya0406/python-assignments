'''Doc: solution <problemset 3>
Question : Modify the above program to print only the words that have no �e� and compute the percentage of the words in the list have no �e.�
Author: divya.natarajan@accenture.com
Date:05/12/2017'''


str=(raw_input("enter the strings"))
strlist=str.split(',')
strlist2=[]
for i in strlist:
  if 'e' not in i and 'E' not in i:
    strlist2.append(i)
print "list of words without 'E'",strlist2    
a=len(strlist)
b=len(strlist2)
per=((float(b)/float(a))*100)
print "\n",per,"% of list's word has no 'E'"