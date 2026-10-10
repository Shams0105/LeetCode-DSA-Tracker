
#Write a code to generate & store tables from 2 to 20 in a tables folder for a 13 yr old


from pathlib import Path

def generateTable(n):
    table = ""  # an empty string to store the table
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"  # append each line of the table to the string

    #a bit complex code below cuz of directory issue(filenotfound err)
    #ow simpler code when u open a new project & write directly into it is
    
    # with open(f'tables/table_{n}.txt' , "w") as f:
    #     f.write(table)

    filePath = Path(__file__).parent / "tables" / f"table_{n}.txt"
    filePath.parent.mkdir(parents=True, exist_ok=True)

    with open(filePath, "w") as f:
        f.write(table)

for i in range (2,21):  #Generate table from 2 to 20
    generateTable(i)

#hence the tables folder was created by me
# while all the txt files inside it was auto generated