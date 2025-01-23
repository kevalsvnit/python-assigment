squares=[]
n=int(input("enter no of elements"))
for i in range(1,n+1):
  k=i*i
  squares.append(k)  

for j in range(n):
  print(squares[j])  