#Basic class & object
#Class = Blueprint
class Employee():
    #These are class attributes
    lang = "Python"
    salary = 1200000

shams = Employee()  # OBJECT
shams.name = "Ahetesham"  #This is an object/instance attribute
print(shams.name , shams.lang , shams.salary)

rohan = Employee()
rohan.name = "Rohan RORO"  #This is an object/instance attribute
print(rohan.name , rohan.salary , rohan.lang)

#Here Salary , Lang are class attributes cuz they directly belongs to class only
#NOTE : name is object attribute

'''
Noun -> Generally the CLass name ex EMPLOYEE , STUDENT , etc
Adjective -> Generally the class attributes ie name , age ,salary , etc
Verb -> The class methods sucha as getSalary(), increment() ,etc

'''