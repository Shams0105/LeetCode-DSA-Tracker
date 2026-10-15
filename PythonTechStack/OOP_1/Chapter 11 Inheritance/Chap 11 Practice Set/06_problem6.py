'''
6. Write __str__() method to print the vector as follows: 
7i + 8j +10k  
'''
class vector:

    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        res = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return res

    #For readable output we use __str__() dunder method specifically for complex outputs
    def __str__(self):
        return f"Vector({self.x }i + {self.y }j + {self.z}k)"  #Used to diplay the result

v1 = vector(1,2,3)
v2 = vector(4,5,6)

print(f"Output after addition of 2 vectors :{v1+v2}")




        