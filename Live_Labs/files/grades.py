f=open("files\data2.txt")
print("*"*20)
print("Name Marks Grade")
print("*"*20)
for row  in f:
    name,marks=row.split()
    if int(marks)>=50:
       grade='Pass'
    else:
       grade='Fail'
    print(name+"    "+marks+"    "+grade)   
    print("*"*20) 