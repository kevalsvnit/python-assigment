def lexico(a):
    a=list(a[::-1])
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
                a[:j]=sorted(a[:j],reverse=True)
                a=a[::-1]
                print(''.join(a))
                return 
    print("No answer")
T=int(input("Enter number of cases:"))
for i in range(T):
    lexico(input("Enter string:"))
