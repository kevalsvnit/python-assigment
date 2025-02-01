fruit_info={}
fruits=[input("enter fruit name") for i in range(3)]
price=[int (input(f"enter the price of {fruits[i]}: ")) for i in range(3)]
for i in range(3):
    fruit_info[fruits[i]]=price[i]

for i in range(3):
    k=input("enter fruit name")
    for i in range(3):  
        if(k==fruits[i]):
            print(f"price of {fruits[i]}:",price[i])
            break
        else:
            print("product not available")    
            break