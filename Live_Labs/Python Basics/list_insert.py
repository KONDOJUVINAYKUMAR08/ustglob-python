marks=[]
#  read 3 marks from the console and  add 3 elements to the list 
# append() is a method  used to add element at the end of the list
for i in range(3): # 0,1,2
    x=int(input("Enter value for x  "))
    marks.append(x)
print(marks)    
# insert() where we want to add 
marks.insert(2,45) # value 45 is added on that index 2
#syntax is insert(index, value)
print(marks)