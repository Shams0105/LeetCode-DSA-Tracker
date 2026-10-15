'''
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module.
'''

import random

no = random.randint(1,100)
a = -1   #for a!=no for the while loop to be true at 1st iteration
guesses = 1
while(a != no):
    
    a = int(input("Guess the number(btw 1-100) : "))

    if(a > no):
        print(f"Your guessed number {a} is higher , try guessing a lower number")
        guesses+=1

    elif(a < no):
        print(f"Your guessed number {a} is too low , try guessing higher")
        guesses += 1    #to count the no of guesses taken 

print(f"Congrats you guessed it right {no}, you took {guesses} number of guesses")

