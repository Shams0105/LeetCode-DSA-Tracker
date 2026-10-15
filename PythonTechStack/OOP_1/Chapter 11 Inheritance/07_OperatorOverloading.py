#Read handbook & clarify 

class Number():

    def __init__(self,n):
        self.n = n 
 
    def __add__(self, other):      #Dunder method to add(operator)
        return self.n + other.n

    def __mul__(self, other):
        return f"Multiplication using op overloading : {self.n * other.n}"

    def __truediv__(self, other):
            return f"Division using op overloading : {self.n / other.n}"

    def __floordiv__(self, other):
                return f"Floor Division using op overloading : {self.n // other.n}"

n = Number(100)
m = Number(200)

print(n + m)   #Cant run if no dunder __add__ method

print(n * m)

print(n / m)

print(n // m)
          