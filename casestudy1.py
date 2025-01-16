
t=int(input())

for i in range(t):
 n=int(input("enter number of box"))  
 x=int(input("enter present position of coin")) 
 s=int(input("enter number of swap"))
 temp=x
 for t in range(s):
  a=int(input("enter value of a:"))
  b=int(input("enter value of b:"))
  if a==temp:
   temp=b
  elif b==temp:
   temp=a



   print("coin is found in position: ",temp)
   
   



    




























