
'''Doc: solution <problemset 2>
   
Question : 8   
Author: divya.natarajan@accenture.com
   
Date:


04/12/2017''' 


import math 
def eval_val(): 
    while True: 
        result = '' 
        str = raw_input('Enter the string : ') 
        if str == 'done' : 
            break 
        else: 
            res=eval(str) 
            print res 
        print result  
eval_val() 
