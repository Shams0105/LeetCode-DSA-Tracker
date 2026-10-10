#Write a code to wipe out the content of a file 

from pathlib import Path
file_path = Path(__file__).with_name("new_file.txt")
with open(file_path, "w") as f:
    f.write("")
    #just write blank to empty the file
    #NOTE this was a file generated in a certain problem which i emptied
