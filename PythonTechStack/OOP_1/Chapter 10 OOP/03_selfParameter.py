"""
================================================================================
                    THE 'SELF' PARAMETER IN PYTHON EXPLAINED
================================================================================
In plain terms: `self` is an explicit reference pointer to the CURRENT instance 
(object) of the class you are dealing with. 

It tells Python: "Work on THIS specific object's variables, not anyone else's."
================================================================================
"""

"""
--------------------------------------------------------------------------------
1. CORE CONCEPT: WHY IS IT MANDATORY IN METHODS?
--------------------------------------------------------------------------------
When you create a class, you write methods (functions inside the class). 
But how does Python know which object called that method?

If you have two user profiles, UserA and UserB, and you update a profile name, 
`self` ensures UserA's name updates without altering UserB's profile data.
"""

class Account:
    def __init__(self, owner_name):
        self.owner = owner_name  # Storing the variable inside 'self'

    # Every regular method MUST take 'self' as the first parameter
    def show_owner(self):
        print(f"This account belongs to: {self.owner}")

# 1. Create two completely independent objects
user_a = Account("Aakash")
user_b = Account("Rohan")

# 2. Call the methods
user_a.show_owner()  # Prints: Aakash
user_b.show_owner()  # Prints: Rohan


"""
--------------------------------------------------------------------------------
2. UNDER THE HOOD: THE SECRET TRANSLATION MECHANIC
--------------------------------------------------------------------------------
When you type this syntactic shorthand:
    `user_a.show_owner()`

Python automatically translates it behind the scenes to this function execution:
    `Account.show_owner(user_a)`

Python passes the object *itself* as the very first argument into the method! 
That is why you must explicitly write `self` inside your class definitions, 
even though you never pass it manually when calling the method.
"""


"""
--------------------------------------------------------------------------------
3. WHAT HAPPENS IF YOU OMIT 'SELF'? (The Classic Crash)
--------------------------------------------------------------------------------
If you define a method without writing `self` as the first argument, 
your code will compile initially, but the moment you try to run it on an object, 
it will crash with a `TypeError`.
"""

class BadExample:
    # ❌ WRONG: Missing the 'self' parameter
    def greet():
        print("Hello World")

obj = BadExample()
# obj.greet() 
# 💥 CRASHES WITH: "TypeError: greet() takes 0 positional arguments but 1 was given"
# Why? Because Python tried to secretly pass `BadExample.greet(obj)`!


"""
--------------------------------------------------------------------------------
4. THE SECRET REVEALED: IS THE WORD 'SELF' A RESERVED KEYWORD?
--------------------------------------------------------------------------------
Technically, NO. `self` is NOT a reserved keyword in Python like `if`, `for`, 
or `def`. It is simply a strong community naming convention. 

You could replace the word `self` with `this`, `me`, or `dsa_prep`, and the code 
will run perfectly fine. However, you should NEVER do this in practice—using 
anything other than `self` will make your code unreadable to other developers 
and tools like Pylance/IntelliSense.
"""

class CustomNameExample:
    def __init__(xyz, name):
        xyz.name = name  # Valid Python syntax, but bad practice!

    def display(xyz):
        print(xyz.name)  # Works exactly like self


"""
================================================================================
SUMMARY LOG FOR YOUR NOTEBOOK
================================================================================
1. `self` binds attributes to the specific object instance inside `__init__`.
2. Every regular method requires `self` as the first parameter to read/write 
   the object's data.
3. Omitting `self` results in a structural argument error during runtime.
================================================================================
"""
