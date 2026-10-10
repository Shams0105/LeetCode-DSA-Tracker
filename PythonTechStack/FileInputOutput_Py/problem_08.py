#8 write a program & make a copy of a text file named "this.txt"

from pathlib import Path

file_path = Path(__file__).with_name("thisP8.txt")
#read & store the data in a variable 
with open(file_path, encoding="utf-8") as f:
    data = f.read()

#Write the stored data in a seperate file usinh 'w' with open
with open('this_copy.txt' , "w") as f:
    f.write(data)  
    print("a new file is successfully generated in the main folder structure \n named \'this_copy.txt\'")