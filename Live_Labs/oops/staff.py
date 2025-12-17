class Staff:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def showInfo(self):
        print("\nName:  ", self.name)
        print("Age:   ", self.age)


# __init__(self, name, age) is a constructor that is executed when we create an object
# self refers to current object

s1=Staff("Vinay", 21)
# print("Name:  ", s1.name)
# print("Age:   ", s1.age)
s1.showInfo()
s2=Staff("Vignesh", 23)
s2.showInfo()