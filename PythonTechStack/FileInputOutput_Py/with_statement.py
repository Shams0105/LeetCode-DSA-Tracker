# With statement is used to open a file and automatically close it after the block of code is executed. 
# It ensures that the file is properly closed even if an error occurs within the block.
# Also no need of worrying about the directory / file path while reading a file,
#  as it automatically takes care of it

# f = open("filetest.txt")
# data = f.read()
# print(data)
# f.close()

#Same can be written using with statement as below:

# with open("filetest.txt") as f:
#     print(f.read())  
#Throws file not found err due to directory / file path issue while reading the file

# No need to close the file explicitly as it is automatically closed after the block of code is executed

from pathlib import Path

file_path = Path(__file__).with_name("filetest.txt")
with open(file_path, encoding="utf-8") as f:
    data = f.read()
    print(data)
