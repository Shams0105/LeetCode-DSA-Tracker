'''
Sometimes we want to run a piece of code when try was successful.
In such cases we use try with else,
where the else block code runs only if try runs fine
'''

try:
    a = int(input("Enter a no:"))
    print(f"The no is {a}")

except Exception as e:
    print(f'Error {e} occured')

else:
    print("try block executed fine , now we're in else")
#ELSE block executed only if there's no err/ try block executed
