import tempConversion

cel=int(input("Enter the temperature in celsius: "))
print("Fahrenheit temp: ", tempConversion.ctof(cel))
fah=int(input("Enter the temperature in fahrenheit: "))
print(f"Celsius temp: {tempConversion.ftoc(fah):.2f}")