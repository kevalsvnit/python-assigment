a=[4,3,2,1]
count=0
for i in range(len(a)):
    
    while a[i]!=i+1:
       correct=a[i]-1
       a[i],a[correct]=a[correct],a[i]
       count+=1


print("minimum no of swap :",count)