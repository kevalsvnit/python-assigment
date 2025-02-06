num=int(input("enter the number"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
    
while sum>=10:
   temp=0
   while sum>0:
     
     temp=temp+(sum%10)
     sum=sum//10
   sum=temp
print(sum)    
    
    
