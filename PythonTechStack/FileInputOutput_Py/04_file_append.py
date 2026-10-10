#Refer  FileTheory.txt for the theory of file handling in python in detail

st = "append 'a' mode is used to append text at the end of the file without overwriting the existing content in the file"
with open("new_file.txt", "a") as f:
    f.write(st)
    print("File created & data written into it successfully")

#NOTE here 'a' mode is used to append into the file in open() function 
#The 'a' mode is used to append text at the end of the file without overwriting the existing content in the file
# it will append the st to new_file.txt as many times as many times u run the code  