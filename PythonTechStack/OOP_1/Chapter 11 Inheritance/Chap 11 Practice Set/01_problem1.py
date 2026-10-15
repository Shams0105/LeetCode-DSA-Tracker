'''
1. Create a class (2-D vector) and use it to create another class representing a 3-D 
vector
'''
class Two_D_Vector():

    def __init__(self , i , j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D vector is : {self.i}i + {self.j}j")

class Three_D_Vector(Two_D_Vector):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f'3D vector using 2D class is : {self.i}i +{self.j}j + {self.k}k')

a = Two_D_Vector(1 , 2)
b = Three_D_Vector(3 , 4 , 5)

a.show()
b.show()


                