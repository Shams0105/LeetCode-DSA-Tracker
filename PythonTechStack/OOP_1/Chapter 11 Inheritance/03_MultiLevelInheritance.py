class emp():
    a = 1

class programmer(emp):    #Inherits emp()
    b = 2

class manager(programmer):   #Inherits both emp & programmer() classes
    c = 3

o = emp()
print(o.a)  #Prints a cuz it has a attribute
#print(o.b , o.c)   Cant print b & c cuz it doesnt have that attr being parent or at top level

o = programmer()
print(o.a ,o.b) #Prints a inherited from emp() & its own attr
#print(o.c)  #Cannot print attr of lower class

o = manager()
print(o.a , o.b ,o.c) #Last class inherits all above classes acc to syntax