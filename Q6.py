
number=int(input("enter the number"))
sum=0
while number>0:
    r=number%10
    sum=sum*10+r
    number=number//10


    print("reversed number:",sum)

    


