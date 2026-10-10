# Write a class calculator capable of finding square , cube & sq root of a number

class calculator:

    #Take n (no) to find its values
    def __init__(self , n):
        self.n = n

    #Square function
    def square(self):
        print(f'The sqaure of {self.n} is {self.n*self.n}')

    #Cube function
    def cube(self):
        print(f'The cube of {self.n} is {self.n* self.n* self.n}')

    #Square root function
    def sqroot(self):
        print(f'The square root of {self.n} is {self.n ** 1/2}')  # ** --> used for raise to

a = calculator(4)  #Passing the number 4 to n
a.square()
a.cube()
a.sqroot()
        