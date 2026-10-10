'''
Refer  FileTheory.txt for the theory of file handling in python in detail

Data after running a py file is stored in RAM
ie all variables ,lists , tuples etc are temporarily stored on RAM which vanishes once a program
is terminated

A py file is runned on RAM making all its data volatile

RAM = Volatile
HDD = Non Volatile

You want ur data to be saved in the file in some cases
Then y RAM y not HDD always
Cuz RAM = very faast 
    HDD = very slow (used only to persist data ie store it)

#FILE
A FILE is a storage device  used to store data
       A py program can interact w the file by
       Write ->writing content to it
       Read  ->Reading content from it
'''

#TYPES OF FILES :- 1] Text file(.txt) , 2]Binary Files (.jpg , .dat , etc)

# TO READ A FILE
from pathlib import Path

file_path = Path(__file__).with_name("FileTheory.txt")
with open(file_path, encoding="utf-8") as f:
    data = f.read()
    print(data)

#This is the code given by copilot as my prev was having err due to directory / file path
#Prev code
'''
f = open(filetest.txt)
data = f.read()
print(data)
f.close()

having err cuz 
Powershell path while running is (Hello) PS C: Users Hello OneDrive Desktop Skills++>
While to read the file it requires 
(Hello) PS C:Users Hello OneDrive Desktop Skills++> wrong one
 c:/Users/Hello/OneDrive/Desktop/Skills++/PythonTechStack/FileInputOutput_Py/01_file.py


'''
