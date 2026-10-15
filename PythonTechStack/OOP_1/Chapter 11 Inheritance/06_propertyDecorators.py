class show():
    a = 1

    @classmethod
    def display(cls):   
        print(f"The class attr using class method to override any Instance attr is {cls.a}")

    @property                #ABSTRACTION & ENCAPSULATION
    def name(self):
        return f"{self.fname} {self.lname}"

    
    @name.setter          #ENCAPSULATED (user just gives a name-> conv into fname , lname)
    def name(self , value):
        self.fname = value.split(" ")[0]   #splits the str where " " occurs into a list
        self.lname = value.split(" ")[1]   #"-----"----" [1]->accesses the lastname ex["Shams" , "Ganjihal"]

s = show()
s.a = 2  

s.name = "Shams Ganjihal" 
print(s.fname , s.lname)
