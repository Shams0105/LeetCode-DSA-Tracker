'''
2. Create a class "Pets" from a class "Animals" and further create a class "Dog" from 
"Pets". Add a method "bark" to class Dog. 
'''

class Animals():
    def display(slef):
        print("Class Animalia")

class Pets(Animals):
    def show(self):
        print("Some animals can be pets")

#Its fine acc to q if we dont add any methods & just use pass in above classes

class dog(Pets):
    @staticmethod   #As no parent class attr accessed
    def bark():
        print("The dog is an animal & a pet which barks: Bhow! , Bhow!")

a = dog()
a.bark()

a.show()
a.display()
