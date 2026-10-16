'''
3. Write a list comprehension to print a list which contains the multiplication table of a 
user entered number.
'''
#named it module3 cuz i am importing it ahead in problem 5 & also used func() for the same
def func():
    n = int(input("enter a no:"))

    table = [n * i  for i in range(1,11)  ]  #Always put the operation at the start
    print(table)
func()

'''
I WENT WRONG AT START
1. Syntax Error inside the List Comprehension (Fatal)
What you wrote: [i for item in (1,11) i * n ]

Why it fails:

Malformed order: The formula for a list comprehension is [expression for variable in iterable].
 You placed i * n at the very end instead of the beginning.

Undefined variable: You named your loop variable item (for item in ...),
 but tried to use i in both the front and the end (i does not exist).

Tuple instead of range: (1, 11) is just a 2-element tuple containing the numbers 1 and 11.
 It will not generate numbers from 1 to 10. To generate a sequence, use range(1, 11).
'''