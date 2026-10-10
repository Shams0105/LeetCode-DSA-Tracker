# 5 A file contains "Donkey" , ganda , acche  multiple times , You need to
# write a program which replaces this word by # times len of tht word  by updating the same file
# ie censoring the words

from pathlib import Path
words = ["Donkey" , "ganda" , 'acche']

#Read the file if it contains donkey
filePath = Path(__file__).with_name('problem5.txt')

with open(filePath , encoding='utf-8') as f:
    content = f.read()

for word in words:
    content = content.replace(word , "#" * len(word))   #replace the donkey word

#write it into the file

with open(filePath , "w") as f:
    f.write(content)  #write the new content in the file

#Successfully writes/ updates the word in the problem4.txt file


