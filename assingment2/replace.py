def replace_custom(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

# Example usage
text = "Hello world, welcome to the programming world."
result = replace_custom(text, "world", "universe")
print(result)
