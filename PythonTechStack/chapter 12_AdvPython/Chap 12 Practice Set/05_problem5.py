'''
5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 
'''
# I tried using importing the 03_problem3 file & then using file i/o 
# but faced errs :
# 1 the name starting w a no (03)->err for import statement
# 2 then when i tried changin the name it threw err: 'table' not defined (can ask someone y)

n = int(input("Enter a number: "))
table = [n*i for i in range(1,11) ]

with open("tables.txt" , "a") as f:
    f.write(str(table) + "\n")

#TABLES AUTO SAVED IN tables.txt as we run the file & enter the no