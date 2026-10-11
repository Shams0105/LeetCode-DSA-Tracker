'''
Static method is used when a function doesnt require self paarmeter
ie it doesnt require any ofthe class attributes .
you use static methods when u  requires zero access to internal class variables or object instances.

'''

class student():
    lang = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The Language is {self.lang} & the salary is {self.salary}")

    @staticmethod         # no need of self as no access to class atrr reqd
    def greet():        
        print("Good Morning")  
        


shams = student()
shams.getInfo()
shams.greet()