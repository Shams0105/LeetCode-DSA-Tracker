"""
================================================================================
          CHAPTER 10: OBJECT-ORIENTED PROGRAMMING (OOP) CHEAT SHEET
================================================================================
OOP is a programming style where you organize your code around real-world 
"objects" (like a User, a Product, a Database Connection) rather than just 
writing a long list of standalone functions.

Why use it? It makes your code modular, reusable, and easy to scale.
================================================================================
"""

"""
--------------------------------------------------------------------------------
1. THE CORE CORE CONCEPT: CLASSES AND OBJECTS
--------------------------------------------------------------------------------
* Class: The blueprint, template, or blank application form. It defines the structure.
* Object: The actual physical instance built from that blueprint. It holds real data.
"""

# The Blueprint
class Smartphone:
    pass 

# The Real World Objects built from the blueprint
phone1 = Smartphone() 
phone2 = Smartphone()


"""
--------------------------------------------------------------------------------
2. ATTRIBUTES (The Variables inside a Class)
--------------------------------------------------------------------------------
Attributes are variables that belong to a class or an object.

A) Class Attributes: 
   - Declared directly inside the class block.
   - Shared by EVERY object made from this class.
   - Saves memory because it is stored only once.

B) Instance Attributes:
   - Declared inside the constructor method using `self`.
   - Unique to each individual object.
"""

class Laptop:
    # A) Class Attribute (Universal rule for all laptops)
    device_type = "Computer" 

    def __init__(self, brand, ram):
        # B) Instance Attributes (Unique values per object)
        self.brand = brand  
        self.ram = ram      

# Creating instances with unique data
laptop1 = Laptop("Dell", 16)
laptop2 = Laptop("MacBook", 8)

# Both objects can read the shared class attribute:
# laptop1.device_type -> "Computer"
# laptop2.device_type -> "Computer"


"""
--------------------------------------------------------------------------------
3. METHODS AND THE MAGIC 'SELF' KEYWORD
--------------------------------------------------------------------------------
* Method: A function that lives inside a class and runs operations on your objects.
* self: A temporary placeholder representing the SPECIFIC object calling the method.

When you run `obj.method()`, Python secretly passes the object into the first 
argument: `Class.method(obj)`. That's why every method needs `self` as its first parameter!
"""

class Calculator:
    def __init__(self, value):
        self.value = value

    # A regular instance method
    def add(self, amount):
        self.value += amount # 'self' points to the specific object being modified


"""
--------------------------------------------------------------------------------
4. THE 4 PILLARS OF OOP (Interview Essentials)
--------------------------------------------------------------------------------
"""

"""
PILLAR 1: INHERITANCE (Code Reuse)
 allows a child class to steal all variables and methods from a parent class 
automatically, preventing code repetition.
"""

# Parent Class
class DataProfessional:
    def __init__(self, name):
        self.name = name
    
    def work(self):
        return "Processing data..."

# Child Class inherits from DataProfessional
class DataEngineer(DataProfessional):
    def build_pipeline(self):
        return "ETL Pipeline active!"

# Deployed check:
# engineer = DataEngineer("Aakash")
# engineer.work()           <- Works! (Inherited from parent)
# engineer.build_pipeline() <- Works! (Unique child method)


"""
PILLAR 2: POLYMORPHISM (Many Forms)
The ability for different classes to have methods with the EXACT same name, 
but executing completely different behaviors.
"""

class Dog:
    def make_sound(self): return "Bark"

class Cat:
    def make_sound(self): return "Meow"

# You can loop through them dynamically without caring about their specific type:
# for animal in [Dog(), Cat()]:
#     print(animal.make_sound()) 


"""
PILLAR 3: ENCAPSULATION (Data Security)
Restricting direct access to an object's variables to prevent accidental 
modification. We hide data by prefixing variables with double underscores `__`.
"""

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance # Private variable! Cannot be accessed directly outside the class.

    # Getter method to safely look at data
    def get_balance(self):
        return self.__balance

    # Setter method to safely update data with rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


"""
PILLAR 4: ABSTRACTION (Hiding Complexity)
Hiding background execution details and only showing the essential interface features 
to the user. (Think of driving a car: you step on the accelerator pedal 
[Interface], but you don't need to know how the engine burns fuel [Background Complexity]).
"""

from abc import ABC, abstractmethod

# Abstract Class (Cannot be instantiated directly, acts as a mandatory rulebook)
class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, file_name):
        pass

class AWSStorage(CloudStorage):
    def upload_file(self, file_name):
        return f"Uploading {file_name} to AWS S3 buckets securely..."


"""
================================================================================
                   OOP SYNTAX DICTIONARY FOR YOUR REFERENCE
================================================================================
* __init__     -> Constructor method. Runs automatically when creating an object.
* __str__      -> Dunder method. Changes what prints when you run print(object).
* super()      -> Function used to trigger the parent class constructor/__init__.
* isinstance() -> Built-in function to verify if an object belongs to a class.
================================================================================
"""

print("File structure compiled successfully. Ready for your notes!")
