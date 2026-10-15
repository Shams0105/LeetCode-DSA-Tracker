class show():
    a = 1

    @classmethod
    def display(cls):   #cls accesses class method & not instance attr
        print(f"The class attr using class method to override any Instance attr is {cls.a}")

s = show()
s.a = 2  #-->Instance attr(normally this is printed but using @classmethod forces it to print class attr)

s.display() #Class attr printed