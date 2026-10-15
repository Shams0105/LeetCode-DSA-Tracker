"""
Chapter 11: Advanced OOP - Operator Overloading
Topic: Complex Number Mathematics using Dunder Methods
"""

class Complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    # Dunder method for addition (+)
    def __add__(self, other):
        # Formula: (a + c) + (b + d)i
        return Complex(self.r + other.r, self.i + other.i)
    
    # Dunder method for multiplication (*)
    def __mul__(self, other):
        # Formula: (ac - bd) + (ad + bc)i
        real_part = (self.r * other.r) - (self.i * other.i)
        imag_part = (self.r * other.i) + (self.i * other.r)
        return Complex(real_part, imag_part)

    # Dunder method to print the object beautifully automatically
    def __str__(self):
        # Formats output as "a + bi" or "a - bi" based on the sign of the imaginary part
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        return f"{self.r} - {abs(self.i)}i"


# --- Execution and Verification ---
# n = 1 + 2i
n = Complex(1, 2)
# m = 3 + 4i
m = Complex(3, 4)

print(f"Number 1: {n}")
print(f"Number 2: {m}")

# 1. Test Addition: Expected (1+3) + (2+4)i = 4 + 6i
sum_result = n + m
print(f"Addition Result: {sum_result}")

# 2. Test Multiplication: Expected (1*3 - 2*4) + (1*4 + 2*3)i = -5 + 10i
mul_result = n * m
print(f"Multiplication Result: {mul_result}")
