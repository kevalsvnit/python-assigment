def rindex_custom(s, sub):

    for i in range(len(s) - len(sub), -1, -1):
        if s[i:i+len(sub)] == sub:
            return i
    raise ValueError("substring not found")
text=input("enter the string")
p=input("engter substring")
result = rindex_custom(text, p)
print(f"The last occurrence of {p} is at index:", result)
  
  