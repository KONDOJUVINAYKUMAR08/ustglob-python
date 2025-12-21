f=open("Live_Labs\Files\data4.txt", 'a')
for i in range(2):
    name=input("Enter name: ")
    marks=input("Enter marks: ")
    f.write(f"{name:<10}{marks}")
    f.write("\n")
f.close()