number = int(input("Enter the number to check: "))

a, b = 0, 1

while b < number:
    a, b = b, a + b

if b == number:
    print(f"{number} is an element of the Fibonacci series")
else:
    print(f"{number} is not an element of the Fibonacci series")
