class Employee:
    def __init__(self, name="Alex", age=45):
        self.name=name
        self.age=age

    def displayEmployee(self):
        print("Name: ",self.name,"Age: ",self.age)

e1=Employee()
e2=Employee("Bharath",22)

e1.displayEmployee()
e2.displayEmployee()

# Returns true if 'salary' attribute exists
print (hasattr(e1, 'salary')) 
# Returns value of 'name' attribute
print (getattr(e1, 'name')) 
# Set attribute 'salary' at 8
setattr(e1, 'salary', 7000) 
print (getattr(e1, 'salary')) 
# Delete attribute 'age'
delattr(e1, 'age') 
print (hasattr(e1, 'age'))