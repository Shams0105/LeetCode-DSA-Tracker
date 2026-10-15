#Super Keyword
'''
The super() keyword is a built-in Python tool that allows a child class to call methods and access 
constructors from its parent class.
1. Avoids Code Repetition: You don't have to copy-paste the attributes of a parent class 
into the __init__ constructor of a child class.
2. Maintainability: If the parent class updates its core layout or variable requirements later, 
the child class automatically receives the update through super() without breaking.
3. Method Overriding Extension: It allows a child class to change the behavior of a parent method 
while still executing the original parent tasks first.
'''

class emp():
    def __init__(self):
        print("Constructor of emp")
    a = 1


class programmer(emp):
    def __init__(self):
        print("Constructor of programmer")    
    b = 2

class manager(programmer):  
    def __init__(self):

        super().__init__()   #ALLOWS TO RUN manager's Parent construcotr as well
        print("Constructor of manager")
    c = 3

# o = emp()
# print(o.a)  

# o = programmer()
# print(o.a ,o.b) 

o = manager()   #manager class executes & prints both classes's constructors using super keyword init
print(o.a , o.b ,o.c) 