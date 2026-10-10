# Write a program to find whether a file is identical to another file

from pathlib import Path

#Read the content from file 1
file_path1 = Path(__file__).with_name("poem.txt")
with open(file_path1, encoding="utf-8") as f:
    data1 = f.read()

#Read the content from file 2
file_path2 = Path(__file__).with_name("filetest.txt")
with open(file_path2, encoding="utf-8") as f:
    data2 = f.read()

#Now compare
if(data1 == data2):
    print("Yes the files are identical")
else:
    print("No the files are not identical")