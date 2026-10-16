# def square(n):
#     return n * n

#Instead u can use it as a variable 

square = lambda x: x*x  #takes x as a variable & performs the specified operation
 
print(f"The square of a no using lambda function is {square(5)}")

'''
Syntax: 
lambda arguments:expressions 
# can be used as a normal function

'''

sum = lambda a,b,c : a+b+c   #Hence it is a variable which acts as a function
print(f"Summation using lambda function is {sum(1,2,3)}")