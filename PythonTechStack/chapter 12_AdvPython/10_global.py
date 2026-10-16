
#this is declared globally 
a = 100
b = 120
def fun():
    
    a = 3 #local variable inside fun not affected by global changes

    global b
    print(f"Local var a : {a} , global b : {b}")

b = 130  #this will also change the blobal var b inside fun()

fun()  #references to local variables inside fun
print(f"Globlaly declared a : {a}") #references global a not a inside fun()

