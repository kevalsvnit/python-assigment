def rfind_custom(s, sub):
    for i in range(len(s) - len(sub), -1, -1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

# Example usage with user input
text = input("Enter the string: ")
p = input("Enter the substring: ")
result = rfind_custom(text, p)
print(f"The last occurrence of '{p}' is at index: {result}")
