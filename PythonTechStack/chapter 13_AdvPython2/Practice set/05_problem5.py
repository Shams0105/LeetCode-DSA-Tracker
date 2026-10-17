"""5. Write a program to find the maximum of the numbers in a list using the reduce 
function. """
#Wrong q interpretation , however the code works for list summation
# from functools import reduce

# l = [1,2,3,4,5,6,7,8,9,10]

# sum = lambda x,y : x + y
# res = reduce(sum,l)
# print(f"the maximum of the list using lambda & reduce function is {res} ")

#SOLUTION
from functools import reduce
l = [ 111,2,65,53,23,201,1]

def larger(a,b):
    if a > b:
        return a
    return b  #Outta if = else

print(reduce(larger , l))
