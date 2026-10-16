def myFunc():
    print("To demonstrate the name of the file which is / from where the code is runned")

myFunc()
print(__name__) 

if __name__ == "__main__":
    #If this code is directly executed by running the file it is present in
    print("We're running the code from where it is present")