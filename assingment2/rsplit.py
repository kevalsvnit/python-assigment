
def rsplit(string,sep=' ',end=float('inf')):
    string=string[::-1]
    l=[]
    str=""
    count,index=0,0
    for i in string:
        if (i==sep  and count<end):
            str=str[::-1]
            l.append(str)
            str=""
            count+=1
        else:
            str+=i
        index+=1
    str=str[::-1]
    l.append(str)
    l=l[::-1]
    return l
L=[]
string=input("enter string:")
sep=input("enter separator:")
print(rsplit(string,sep,2))