lengthfeet=float(input("enter lenth in feet"))
conversion_factors = [12, 1 / 3, 1 / 5280, 304.8, 30.48, 0.3048, 0.0003048]

print("\nChoose the conversion option:")
print("1. Inches") 
print("2. Yards") 
print("3. Miles")
print("4. Millimeters")
print("5. Centimeters")
print("6. Meters")
print("7. Kilometers")

option=int(input("enter number according to choise"))

if 0 < option <= len(conversion_factors):
    convertedlength=lengthfeet*conversion_factors[option-1]
    print("converted length is",convertedlength)

else:
 print("entered invalid option")       