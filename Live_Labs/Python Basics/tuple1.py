# tuple is similar to list but values can not be modified-immutable
# all elements are placed in () brackets 
marks=(23,45,56)
print(type(marks))
#marks[0]=45

#to change elements 
marks=list(marks)
marks[0]=45
marks=tuple(marks)
print(marks)