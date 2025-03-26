
t = int(input("Enter number of test cases: "))

for _ in range(t):
    a, b = map(int, input("Enter two space-separated integers (A and B): ").split())
    
    count = 0
    
    for i in range(a, b + 1):
        if int(i**0.5) ** 2 == i:
            count += 1
            
    print(count)
