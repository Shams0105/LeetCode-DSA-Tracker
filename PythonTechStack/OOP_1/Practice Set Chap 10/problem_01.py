# Create a class programmer for storing info of few programmers working @ Microsoft
class Programmer:
    company = "Microsoft"  #Since all are working at Microsoft

    #Constructor
    def __init__(self, name , salary , pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        print("Dunder object created for storing programmer's data")

p1 = Programmer("shams" , 13000000 , 416010)
print(p1.name , p1.salary , p1.pincode , p1.company)

p2 = Programmer("ahmed" , 13000000 , 416010)
print(p2.name , p2.salary , p2.pincode , p2.company)

p3 = Programmer("iramnaz" , 13000000 , 416010)
print(p3.name , p3.salary , p3.pincode , p3.company)
    
