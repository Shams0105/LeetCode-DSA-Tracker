# 4 A file contains "Donkey" multiple times , You need to
# write a program which replaces this word by ###### by updating the same file

from pathlib import Path
word = "Donkey"

#Read the file if it contains donkey
filePath = Path(__file__).with_name('problem4.txt')

with open(filePath , encoding='utf-8') as f:
    content = f.read()

contentNew = content.replace(word , "######")   #replace the donkey word

#write it into the file

with open(filePath , "w") as f:
    f.write(contentNew)  #write the new content in the file

#Successfully writes/ updates the word in the problem4.txt file


