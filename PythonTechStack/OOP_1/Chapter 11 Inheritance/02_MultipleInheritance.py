'''
• Definition: A design where one single Child class inherits directly from two or more completely 
              independent Parent classes at the same time. 
              This merges separate feature sets into a unified hybrid entity.
• Real-World Analogy: Think of a multi-functional device:
	• Parent 1: Digital Camera (knows how to take photos).
	• Parent 2: GPS Navigator (knows how to track map coordinates).
	• Child: Travel Smartphone (inherits directly from both 
    Parent 1 and Parent 2, allowing it to take high-quality geotagged photos with embedded map locations).
'''
#Inheritance:-

class Employee:
    company = "ITC"
    def show(self):  
        print(f"The name of the emp is : {self.name} & his salary is {self.salary} , company :{self.company}")

class coder:
    language = "Java"
    def printLang(self):
        print(f"Your language is {self.language}")


class Programmer(Employee , coder):   #Multiple classes inherited
    company = "ITC INFOTECH"

    def showLang(self):  
        print(f"The name of the emp is : {self.name} & his lang efficiency is in {self.Lang}")

#Object creation
a = Employee()
a.name = "Shams"
a.salary = "1300000"

b = Programmer()
b.name = "Ahmed"     
b.salary = 1400000  
b.Lang = "Python"   

#Method calls
a.show()
b.show()  #Inherited child class
b.printLang() #Inherited class 2




