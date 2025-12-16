x=[23,45,56,78,90]
y=x    # y gets ref of x . both refers to same memory location
print(id(x))
print(id(y))
x[0]=90
print(x)
print(y)