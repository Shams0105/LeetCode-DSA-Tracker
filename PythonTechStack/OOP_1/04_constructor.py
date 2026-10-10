# VERY IMP CONCEPT CONSTRUCTOR
'''
__init__() is a special method which is first run as soon as the object is created. 
__init__() method is also known as constructor. 
It takes ‘self’ argument and can also take further arguments.
'''


class student():
    lang = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The Language is {self.lang} & the salary is {self.salary}")

     #Dunder Method ; Called automatically 
    def __init__(self , name , salary , lang):    #Constructor
        self.name = name
        self.salary = salary
        self.lang = self.lang
        print("Object creation using dunder method __init__() called auto")




shams = student("SHAMS" ,13000000 , "Python") #hence using constructor we can directly pass the values here
print(shams.name , shams.salary , shams.lang)
 