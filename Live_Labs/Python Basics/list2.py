x=[23,45,56,78,90]
y=[23,45,56,78,90]
# == checks both lists have same values 
# is check memory address
print(x==y)
print(x is y)
print(id(x))
print(id(y))
y=x 
print(x==y)
print(x is y)
