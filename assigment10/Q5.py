import numpy as np
import matplotlib.pyplot as plt
import random

# Define the polynomial function f(x)
def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Roots at x = 1, 2, 3

# Step 1: Random probing to find a valid interval [a, b] such that f(a)*f(b) < 0
def find_initial_interval(f, lower=-10, upper=10, max_attempts=1000):
    for _ in range(max_attempts):
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
        if a > b: a, b = b, a  # Ensure a < b
        if f(a) * f(b) < 0:
            return a, b
    raise ValueError("Failed to find a valid interval with opposite signs.")

# Step 2: Bisection Method
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        iterations.append([i, a, b, c, fc])
        if abs(fc) < tol or (b - a) / 2 < tol:
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return np.array(iterations)

# Step 3: Plot the root finding process
def plot_iterations(iterations):
    midpoints = iterations[:, 3]
    f_values = iterations[:, 4]
    plt.plot(midpoints, f_values, 'bo-', label='f(midpoint)')
    plt.axhline(0, color='red', linestyle='--')
    plt.title("Bisection Method Convergence")
    plt.xlabel("Midpoint")
    plt.ylabel("f(Midpoint)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main execution
a, b = find_initial_interval(f)
iterations = bisection_method(f, a, b)
print("Iterations (Step, a, b, midpoint, f(midpoint)):\n", iterations)

plot_iterations(iterations)
