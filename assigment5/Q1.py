#function to find max xor 
def find_maxxor(l,r):
    max=0
    for i in range (l,r+1):
      for j in range(i,r+1):
         current_xor=i^j
         if current_xor>max:
          max=current_xor
    return max

#taking input

l=int(input())
r=int(input())

print("maximum xor is",find_maxxor(l,r))
