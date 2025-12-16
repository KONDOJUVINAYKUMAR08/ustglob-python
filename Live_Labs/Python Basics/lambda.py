#lambda is used for light weight function
# it can take any parameters and has only one  expression.
# syntax : lambda parameters list : expression
# it is anonynmous function and no return statement
x=lambda a,b : a+b  # we assign a function to a variable x 
# x gets the address of the function lambda 
print(x)
print(x(4,5))