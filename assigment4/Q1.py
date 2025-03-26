t=int(input("enter testcase"))
for i in range(t):
    string=str(input("enternstring"))
    k=len(string)
    count=0
    for i in range(0,len(string)//2):
     
     a=ord(string[i])
     b=ord(string[len(string)-i-1])
         
     if string[i]!=string[len(string)-i-1]:
           if (a)>(b) :
               
               count=count+(a-b)
           else:
               count=count+(b-a)


    print(count) 

     

    