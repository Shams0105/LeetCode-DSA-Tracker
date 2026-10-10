class Employee():
    #These are class attributes
    lang = "Python"
    salary = 1200000

shams = Employee()  # OBJECT

shams.lang = "JavaScript"  #This is an object/instance attribute
print(f"It will print instance attr for lang which is :{shams.lang, shams.salary}")

#Here it will print JS & not Python cuz of:
#NOTE: Instance attributes take preferance over class attributes during assignment & retrieval

#NOTE : Instance is an object property it is related to that 
#       particular object only , hence it doesnt affect or change anything in class blueprint