class Father:
    # adding __ before method or attribute name it becomes private.....
    def __f_bike(self):  
        print("Take  a ride of fathers Bike ")   
class Son(Father):  
    def s_bike(self):  
        print("IT is my bike, i take a ride ")  
s = Son()  
s.s_bike()  
# if we try to access private methods or attributes it throws error....
s.__f_bike()  