'''
3. Create a class ‘Employee’ and add salary and increment properties to it
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary. 
'''

class Employee():
    salary = 250
    increment_per = 20

    @property
    def salaryAfterInc(self):
        return (self.salary + self.salary * (self.increment_per/100))

    @salaryAfterInc.setter
    def salaryAfterInc(self,salary):
        self.increment_per = ((salary / self.salary) -1) * 100


s = Employee()

print(s.salaryAfterInc)
s.salaryAfterInc = 301 
print(s.increment_per)