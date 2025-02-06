t=int(input("enter value of testcase :"))

for i in range(t):
   height=1
   n=int(input("enter number of cycles:")) 
   if(n==0) :
      height=1
   else:

    for i in range(1,n+1):
     if i%2==1:
        height=height*2
     else:
        height=height+1   
   print("height is:",height)        