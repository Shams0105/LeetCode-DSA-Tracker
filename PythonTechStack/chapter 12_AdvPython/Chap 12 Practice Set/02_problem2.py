'''
2. Write a program to print third, fifth and seventh element from a list using enumerate 
function. 
'''
l = [0,1,2,3,4,5,6,7,8,9,10]
for i , e in enumerate(l):
    if(i == 2 or i == 4 or i == 6):
        print(f"The {i+1} element is {e}")

#OWNNN