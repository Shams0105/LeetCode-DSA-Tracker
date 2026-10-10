# Create a class with a class attribute a ; create an object from it & set 'a' 
# directly using object.a = o . Does this change the class attr?

class Demo :
    a = 4

object = Demo()

#Class attribute is printed cuz instance attr is not present
print(object.a)

#Instance object created hence it is printed now
object.a = 0
print(object.a)

print(f'class attr doesnt change even after creating instance attr \n Class Attr:{Demo.a} & Instance Attr:{object.a}')