#Imp concept
'''
A list comprehension is a concise, one-line syntax in Python used to construct a new list by
transforming or filtering an existing iterable (like a list, range, or string).

It replaces multi-line for loops and append() calls with cleaner, faster code
'''
#traditional way

# numbers = [1, 2, 3, 4, 5]
# squares = []

# for n in numbers:
#     if n % 2 == 0:
#         squares.append(n * n)

# print(squares)  # [4, 16]

#Using List Comprehension THE MAIN CONCEPT
numbers = [1, 2, 3, 4, 5 , 6, 8]

squares = [n * n for n in numbers if n % 2 == 0]

print(squares)  # [4, 16]

