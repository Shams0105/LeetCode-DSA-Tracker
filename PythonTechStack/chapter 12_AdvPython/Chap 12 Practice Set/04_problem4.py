'''
4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’.
'''
try:
    a = int(input("ENter numerator "))
    b = int(input("Enter denominator "))
    print(a/b)
except ZeroDivisionError as e:
    print(f"INFINITY , cant divide by 0")