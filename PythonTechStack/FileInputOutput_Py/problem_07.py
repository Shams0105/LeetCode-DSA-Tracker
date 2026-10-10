# Write a program to find out where python is present from problem no 6


from pathlib import Path
filePath = Path(__file__).with_name("LogFileP6.txt")

with open(filePath , encoding='utf-8') as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if('python' in line):
        print(f'Yes python is present at line number :{lineno}')
        break # used to break the loop once the solution is reached --> reduces TC & SC
    lineno+=1

else:
    print("Python is not present")  # for -else loop

#Else is executed only when for loop exhauts ow it is not
    
