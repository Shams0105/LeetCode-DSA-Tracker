'''
5. Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them.
'''

class vector:

    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        res = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return res

    def __mul__(self, other):
        res = self.x * other.x + self.y * other.y + self.z * other.z   #dot prod -> Mul & add
        return res

    #For readable output we use __str__() dunder method specifically for complex outputs
    def __str__(self):
        return f"Vector({self.x }i, {self.y }j, {self.z}k)"  #Used to diplay the result

#Testing the vector implementation
v1 = vector(1,2,3)
v2 = vector(4,5,6)

print(f"Output after addition of 2 vectors :{v1+v2}")
print(f"Output after dot product of 2 vectors :{v1*v2}")




        