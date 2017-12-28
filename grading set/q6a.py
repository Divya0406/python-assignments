'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 28/12/2017
   Question   : Create a program which asks the user for 3 numbers representing the year, month and day e.g 1982 10 08 and then outputs in the form 8th October 1982.'''
   
import calendar

'''function to change date
input: list["yyyy","mm","dd"]
output: dd mon yyyy'''
def dat(a):
    if a[2]=="01" or a[2]=="21" or a[2]=="31":
      c=a[2]+"st"
      print c,calendar.month_abbr[int(a[1])],a[0]
    elif a[2]=="02" or a[2]=="22":
      c=a[2]+"nd"
      print c,calendar.month_abbr[int(a[1])],a[0]
    elif a[2]=="03" or a[2]=="23": 
      c=a[2]+"rd"
      print c,calendar.month_abbr[int(a[1])],a[0]
    else:
      c=a[2]+"th"
      print c,calendar.month_abbr[int(a[1])],a[0]
  

try:
  a=raw_input("enter the date string in yyyy mm dd format:")
  a=a.split(" ")
  if len(a[0])!=4:
    print "enter the correct year"
  elif int(a[1]) not in [1,2,3,4,5,6,7,8,9,10,11,12]:
    print "enter the correct month"
  else:  
    dat(a)
except IndexError:
  print "enter the input in the form of yyyy mm dd"
