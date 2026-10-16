'''
There are many built-in exceptions which are raised in python when something goes 
wrong. 
Exception in python can be handled using a try statement. The code that handles the 
exception is written in the except clause.
'''
#When the exception is handled, the code flow continues without program interruption. 

try:
    a = int(input("enter a number:"))   #Suppose user enters a string
    print(a) #Returns ValueError & crashes the program

except Exception as e:   #Handles the error
    print(e)

print("Executes even if the program has err in any of above lines")