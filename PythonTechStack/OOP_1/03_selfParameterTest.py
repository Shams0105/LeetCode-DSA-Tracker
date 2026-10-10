class student():
    lang = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The Language is {self.lang} & the salary is {self.salary}")

    def greet(xyz):        #can use anything but bad practice always use 'self'
        print("Good Morning")  #Throws err if self was not passed as an arg when called
        


shams = student()
shams.lang = "Javascript" #an instance attribute preferred over class attribute

shams.getInfo()
shams.greet()
# employee.getInfo(shams) -> above code is auto converted into this  by Py
# Its fine if u run any of the above 2 
# As u can see we are passing an argument which is accepted by 'self' in the fn we defined
# If u dont write the self arg [(can be any self is not a reserved keyword can use anything like this
# xyz , etc) ->But always use self to make the code readable in development]
# so if u dont write self then the fn takes 0 arg while 1 is given while calling it 
# ie shams.getInfo() = employee.getInfo(shams) -->throws err of arg 1 given , accepts 0