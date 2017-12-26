'''problemset : Gradingset
   Author     : divya.natarajan
   Date       : 16/12/2017
   Question   :Write a Program to Implement a the linear search algorithm. Test that it works with items in and not in the list (a) Add a counter to report how many searches have been done for each item searched for. (b) Add the functionality to add an item to the list if it is not found.'''

'''function to search the element in the list
   input parameters: search element,list
   output: index'''
def search(a,l1):
  count=0
  for i in l1:
    count+=1
    if a==i:
      print "searched the list ",count,"times"
      print "the number is found at the index:", l1.index(a)
      break
  if count==len(l1):
    print("element is not found in the list. hence added to the list")
    add(a,l1)

'''if the element is not in the list it is added to the list'''
def add(a,l1):
  l1.append(a)
  print "the new list is",l1


l1=[14,23,56,41,78,45,13,90,141]
print "the lsit is : ",l1
a=int(raw_input("\nEnter the number to be searched:"))
search(a,l1)


#testfunction
def test_fun():
  print "\n----test_function----"
  print "for 78"
  search(78,l1)
  print "for 1141"
  search(1141,l1)

test_fun()  
