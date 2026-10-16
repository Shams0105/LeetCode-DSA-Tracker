'''
Type hints are added using the colon (:) syntax for variables and the -> syntax for 
function return types. 
'''

# Variable type hint 
age: int = 25 
# age.   remve the cmnt & see ,py provides all the list of methods builtin available for int

name : str = "Shams"
#name.

# Function type hints 
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 
# Usage 
print(greeting("Alice"))  # Output: Hello, Alice! 

def addition(a : int , b : int ) -> int:
    return a + b

addition(1,3)  #prompts to pass int before typing the args.
