def count_custom(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

# Example usage with user input
text = input("Enter the string: ")
sub = input("Enter the substring to count: ")
result = count_custom(text, sub)
print(f"The substring '{sub}' appears {result} times in the string.")
