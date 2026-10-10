# With statement is used to open a file and automatically close it after the block of code is executed. 
# It ensures that the file is properly closed even if an error occurs within the block.
# Also no need of worrying about the directory / file path while reading a file,
#  as it automatically takes care of it

# f = open("filetest.txt")
# data = f.read()
# print(data)
# f.close()

#Same can be written using with statement as below:

# with open("filetest.txt") as f:
#     print(f.read())  
#Throws file not found err due to directory / file path issue while reading the file

# No need to close the file explicitly as it is automatically closed after the block of code is executed

from pathlib import Path

file_path = Path(__file__).with_name("filetest.txt")
with open(file_path, encoding="utf-8") as f:
    data = f.read()
    print(data)

'''
Computers do not natively understand letters, emojis, or symbols; they only understand binary numbers 
(0s and 1s).
An encoding is a translation key or rulebook that tells the computer how to map binary numbers to 
readable characters.
• utf-8 (Universal Character Set Transformation Format—8-bit) is the absolute world standard encoding 
rulebook. It covers almost every character from every language on earth, including emojis.
• The Problem: If you don't specify encoding="utf-8", Python will fall back to your operating system's
 default setting (e.g., cp1252 on many Windows setups). If your file contains accents, Hindi characters
 , or emojis, a different rulebook will try to read them, 
 causing your code to crash with a UnicodeDecodeError or
   display scrambled text like æøå (known as mojibake).
Always include encoding="utf-8" to make your code bulletproof across Windows, Mac, and Linux.
'''