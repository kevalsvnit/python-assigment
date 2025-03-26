t = int(input())
result = []

for i in range(t):
    k = int(input())
    if k % 2 == 0:
        pieces = (k // 2) * (k // 2)
    else:
         pieces = (k // 2) * (k // 2 + 1)
    result.append(pieces)

for pieces in result:
    print(pieces)
