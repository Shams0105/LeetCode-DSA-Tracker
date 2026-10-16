'''
1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same.
'''
from pathlib import Path
try:
    filePath = Path(__file__).with_name("1.txt")
    with open(filePath , encoding="utf-8") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)