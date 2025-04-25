#Write a program to make the length of each element 15 of a given Numpy array and the
#string centred, left-justified, right-justified with paddings of _ (underscore).
import numpy as np

# Example NumPy array with string elements
arr = np.array(['apple', 'banana', 'cherry', 'date'])

# Make the length of each element 15 with different justifications
centered = np.char.center(arr, 15, fillchar='_')
left_justified = np.char.ljust(arr, 15, fillchar='_')
right_justified = np.char.rjust(arr, 15, fillchar='_')

# Printing the results
print("Centered:")
print(centered)

print("\nLeft-justified:")
print(left_justified)

print("\nRight-justified:")
print(right_justified)
