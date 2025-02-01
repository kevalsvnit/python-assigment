text=input("enter the string")
result=''
for i in range(len(text)):
    if i%2==1:
     result=result+text[i].upper()

    else:
       result=result+text[i].lower()

print(result)       

    