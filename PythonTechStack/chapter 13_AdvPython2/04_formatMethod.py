'''
Formats the values inside the string into a desired output. 
template.format(p1,p2...) 
Syntax: 
"{} is a good {}".format("harry", "boy")   #1. 
"{} is a good {o}".format("harry", "boy")  #2. 
# output for 1: 
# harry is a good boy  
# output for 2: 
# boy is a good harry 
'''

#NOTE : This is a old method overtaken by f"string" but u shld know it

"{} is a good {}".format("harry", "boy")   #1. by default it has {1}.....{0}
"{} is a good {0}".format("harry", "boy")  #2. 
# output for 1: 
# harry is a good boy  
# output for 2: 
# boy is a good harry  