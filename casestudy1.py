
t=int(input())

for i in range(t):
 n=int(input())  
 x=int(input()) 
 s=int(input())
 temp=x
 for t in range(s):
  a=int(input())
  b=int(input())
  if a==temp:
   temp=b
  elif b==temp:
   temp=a



   print("coin is found in ",temp)
   
   



    




























