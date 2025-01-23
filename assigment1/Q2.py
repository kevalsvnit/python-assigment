import random
randomint = [random.randint(0, 1) for i in range(100)]
currentrun=0
maxrun=0
for i in range(100):
    if randomint[i]==0:
        currentrun+=1
        if currentrun>maxrun:
            maxrun=currentrun

    else:
        currentrun=0        
           
    

print(randomint)
print(maxrun)     