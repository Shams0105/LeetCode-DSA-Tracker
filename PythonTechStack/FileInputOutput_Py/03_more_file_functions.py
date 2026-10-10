# TO READ A FILE
from pathlib import Path

file_path = Path(__file__).with_name("filetest.txt")  #by default the mode for open() function is 'r' which is used to read a file
with open(file_path, encoding="utf-8") as f:

    #1]readlines() function reads all the lines from the file at a time and returns a list of lines in the file
    # data = f.readlines()
    # print(data ,type(data))  #readlines() returns a list of lines in the file

    #2] for readline() function it reads a single line from the file at a time
    line1 = f.readline()
    print(line1 ,type(line1))  #readline() returns a string of a single line in the file
    line2 = f.readline()
    print(line2 ,type(line2))
    line3 = f.readline()
    print(line3 ,type(line3))

    # while (line != ""):  #this loop will run until the end
    #     print(line)
    #     line = f.readline()  #reads the next line from the file

    #reads as many lines as many times u call the readline() fn
    f.close()  #closes the file after reading it