equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for number in range(1, 10001):
    remainder = number % 5
    equivalence_classes[remainder].append(number)
# Print equivalence classes
print("Equivalence Classes:")
for remainder, numbers in equivalence_classes.items():
    print(f"Remainder {remainder}: {numbers[:10]}...")  # Print first 10 numbers for brevity

# Check validity
combined_numbers = []
for numbers in equivalence_classes.values():
    combined_numbers.extend(numbers)
combined_numbers.sort()

# Checking if union of all equivalence classes is the original set {1, 2, ..., 10000}
original_set = list(range(1, 10001))
if combined_numbers == original_set:
    print("equivalent classes are valid")
