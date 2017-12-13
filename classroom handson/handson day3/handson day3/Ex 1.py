'''python handson 
  Day 3
 Date : 12/12/2017
 Question :1'''


inventory= {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
                }
                
'''a) Add a key to inventory called 'pocket'. 
b) Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.'''
inventory['pocket']=['seashell','strange berry','lint']
print(inventory)

'''c) .sort()the items in the list stored under the 'backpack' key.'''
inventory['backpack'].sort()
print(inventory)

'''Then .remove('dagger') from the list of items stored under the 'backpack' key.'''
inventory['backpack'].remove('dagger')
print(inventory)

'''Add 50 to the number stored under the 'gold' key.'''
a=inventory['gold']
inventory['gold']=a+50
print(inventory)

