#1 Write a program to check if a word is present in a file or not

from pathlib import Path

file_path = Path(__file__).with_name("poem.txt")
with open(file_path, encoding="utf-8") as f:
    content = f.read()
    if('Twinkle' in content):
        print("The word \'Twinkle'\ is present in the poem")
    else:
        print("The word \'Twinkle'\ is not present in the poem")