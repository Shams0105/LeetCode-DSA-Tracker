"""4. Write a program to filter a list of numbers which are divisible by 5."""

# l = [] #My method
# for i in range(10):
#     n = int(input("Enter any no:"))
#     l.append(n)
# print(l)

# def fun(x):

#     if x % 5 == 0:
#         return True
#     return False

# #Filter method
# only5 = filter(fun,l)
# print(list(only5))  #Necessary to conv to list for visivle /readable op

def is_divisible_by_5(n):
    """Returns True if the number is divisible by 5, otherwise False."""
    if n % 5 == 0:
        return True
    return False

# 1. Initialize an empty list to store user inputs
numbers = []

# 2. Get 10 numbers from the user
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# 3. Use the filter method to extract numbers divisible by 5
# filter() returns an iterator, so we convert it back to a list
filtered_numbers = list(filter(is_divisible_by_5, numbers))

# 4. Print the results
print("\nOriginal list:", numbers)
print("Numbers divisible by 5:", filtered_numbers)
