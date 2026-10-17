'''
3. A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers
7
14
.
.
.
'''
#My method , can also use enumerate to print its indices as well
# table = [ 7 * i for i in range(1,11)]
# for t in range(len(table)):
#     print(table[t] , end="\n")

#Harry's method
table = [ str(7 * i) for i in range(1,11)] #convert to str cuz join accepts str

s = "\n".join(table)
print(s)

