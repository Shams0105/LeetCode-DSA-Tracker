#Inheritance:-

class Employee:
    company = "ITC"
    def show(self):   #Here self = a from obj created below
        print(f"The name of the emp is : {self.name} & his salary is {self.salary} , company :{self.company}")

#Wihtout using inheritance:

# class Programmer:
#     company = "ITC Infotech" 
#     def show(self):  #Copied from parent cl;ass to inherit -->Manual inheritance
#         print(f"The name of the emp is : {self.name} & his salary is {self.salary}")

#     def lang(self):
#         print(f"The name of the emp is : {self.name} & his lang is {self.lang}")

#RUns fine for small code but every time u have to make changes u nee dto copy paste it from parent class
# to as many child inherited class u make which is tedious & inefficent

#INHERITANCE:- solves this issue

class Programmer(Employee): #Programmer(child) --> Inherits --> Employee(parent)
    company = "ITC INFOTECH"

    def showLang(self):  #Here self = b from obj created below
        print(f"The name of the emp is : {self.name} & his lang efficiency is in {self.Lang}")

a = Employee()
a.name = "Shams"
a.salary = "1300000"

b = Programmer()
b.name = "Ahmed"     #Inherited from show()
b.salary = 1400000   #"------"-------"----"
b.Lang = "Python"    # Specific showLang attr

print(f" Name :{a.name} , Salary : {a.salary} , company A: {a.company} \n inheritance ->Name : {b.name} , Salary :{b.salary} & efficency in : {b.Lang} , Comapny B : {b.company}")

a.show() #Parent class
b.show()  #Inherited child class
b.showLang() #Specific child class method




