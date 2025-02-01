t=int(input("enter no of testcases"))
for i in range(t):
    num=int(input("enter the number"))
    count =0
    k=num
    while(num>0):
       r=num%10
       if r!=0 and k%r==0:
          count=count+1
       num=num//10
    print(count)
