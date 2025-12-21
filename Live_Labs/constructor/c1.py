class Empolyee:
    def __init__(self, name, id):
        self.id=id
        self.name=name

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}.")

e1=Empolyee("John",101)
e2=Empolyee("Kyle",102)
# accessing display() method to print employee 1 information 
e1.display()
# accessing display() method to print employee 2 information 
e2.display()