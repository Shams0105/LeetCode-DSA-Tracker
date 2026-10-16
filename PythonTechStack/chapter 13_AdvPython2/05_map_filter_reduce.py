'''
Map applies a function to all the items in an input_list. 

Syntax. 
1]map(function, input_list) 
# the function can be lambda function 

2] Filter creates a list of items for which the function returns true. 
list(filter(function)) 
# the function can be lambda function 

3] Reduce applies a rolling computation to sequential pair of elements. 
from functools import reduce 
val=reduce (function, list1)        
# the function can be lambda function 
54 
55 
 
If the function computes sum of two numbers and the list is [1,2,3,4]
'''
#used for reduce function 
from functools import reduce


#MAP - Used to apply a function on every element 

l = [2,3,4,5,6,7,8]
square = lambda x : x*x

sqlist = map(square , l) #maps every list element to the lambda function
print(list(sqlist))  #we use list before ow it prints complex object not the list   


#FILTER - iterates over every element & checks if it satisfies the codition (T/F)
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even , l)  #1st arg = func(even) , 2nd arg = list
print(list(onlyEven))  #Checks every element & returns the element evaluated to true in the list


#REDUCE
def sum(a,b):
    return a + b # adds consecutive list nos see the handbook ex fpr best visualization

#Adds like a tree first 2 then the res & the next element & sooo onn......
res = reduce(sum,l)
print(f"The addition of a list using reduce function is {res}")

#reduce takes 1st arg as function & the 2nd arg as list

#using lambda

mul = lambda x,y : x*y  #NOTE the before colon : after colon args must be same (cant use x : x*y)
res = reduce(mul,l)
print(f"The multiplication of a list using reduce function is {res}")








