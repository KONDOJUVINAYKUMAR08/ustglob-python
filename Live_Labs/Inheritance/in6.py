class A:
    def show(self):
        print("It is from A")
class B:
    def show(self):
        print("It is from B")
class C(B,A):                   #multiple inheritance
    def print(self):
        print("It is from C")
c=C()        
c.print()
c.show()
