class Father:  

    def buyingBike(self):  
        print("Buy Scooty")  
class Son(Father):  
    def buyingBike(self):       #method overriding  
        print("Buy Royal Enfield Classic 350 CC") 
s=Son()
s.buyingBike()
