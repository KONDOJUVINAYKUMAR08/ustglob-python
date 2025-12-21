f=open("Live_Labs\Files\data5.txt", 'a')
f.write("name        m1   m2   total   grade")
for i in range(2):
    name=input("Enter name: ")
    m1=int(input("Enter marks of m1: "))
    m2=int(input("Enter marks of m2: "))
    grade="fail"
    total=m1+m2
    if(m1>=50 and m2>=50):
        grade="pass"
    f.write(f"\n{name:<12}{m1:<5}{m2:<5}{total:<8}{grade}")
f.close()