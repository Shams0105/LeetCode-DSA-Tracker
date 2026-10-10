# Write a program to mine a log file & find out whther it contain 'python'
# in HTML -> Lorem435 used to generate a large text 
from pathlib import Path
filePath = Path(__file__).with_name("LogFileP6.txt")
with open(filePath , encoding='utf-8') as f:
    data = f.read()
    if 'python' in data:
        print("Yes the log file contains 'python")
    else:
        print("No the log file doesnt contain python")
