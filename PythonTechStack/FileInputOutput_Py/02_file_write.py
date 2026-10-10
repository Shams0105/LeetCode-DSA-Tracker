#Refer  FileTheory.txt for the theory of file handling in python in detail

st = "TO create a new file & write into it in py uisn g open() function with 'w' mode , This will save it in the main project folder directry where the py file is present"
with open("new_file.txt", "w") as f:
    f.write(st)
    print("File created & data written into it successfully")

#NOTE here 'w' mode is used to write into the file in open() function 