# Question:
# Take N (N >= 10) random 2-dimensional points represented in Cartesian coordinate space.
# Store them in a numpy array. Convert them to polar coordinates.

import numpy as np

# Set the number of points (N >= 10)
N = 10


cartesian_points = np.random.rand(N, 2) * 20 - 10  # Random values in range [-10, 10]

# Separate x and y
x = cartesian_points[:, 0]  
y = cartesian_points[:, 1]  

# Convert to polar coordinates
r = np.sqrt(x**2 + y**2)  # Use x^2 + y^2 to calculate the distance

theta = np.arctan2(y, x)

# Combine r (radius) and theta (angle) into a polar coordinate array
polar_points = np.column_stack((r, theta))

# Display the results
print("Cartesian Coordinates:\n", cartesian_points)
print("\nPolar Coordinates (r, theta in radians):\n", polar_points)
