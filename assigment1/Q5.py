student_name = []
print("Enter the student names:")

# Collect student names
for i in range(10):
    name = input(f"Student {i+1} name: ")
    student_name.append(name)

# Reverse and print the names
print("\nReversed Student Names:")
for name in student_name:
    if len(name) > 15:
        updatename = name[:15]
        reversename = updatename[::-1] 
    else:
        reversename = name[::-1]  # Reverse the name directly
    
    print(reversename)
