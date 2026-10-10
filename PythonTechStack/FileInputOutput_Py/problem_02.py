"""
The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
previous Hi-score. You need to write a program to update the Hi-score whenever the
game() function breaks the Hi-score.
"""
import random
from pathlib import Path

def game():
    print("you are playing the game")
    score = random.randint(1, 100)
    print("your score is ", score)

    #Fetch the previous hi-score from the file ie read the file and store the hi-score in a variable
    file_path = Path(__file__).with_name("hiscore.txt")
    with open(file_path, encoding="utf-8") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
    print(f"previous/your hi-score is {hiscore}")

    #Logic to update the hi-score if the current score is greater than the previous hi-score
    if(score > hiscore):
        #Write this hiscore to the txt file
        #normal with open() method will not work here as it will throw file not found error 
        # due to directory / file path issue while reading the file


        file_path = Path(__file__).with_name("hiscore.txt")

        with open(file_path, "w") as f:
            f.write(str(score)) #USed str becaise write() function only takes string as input
            print("congrats! you have just broken the hi-score")


    return score

game()

