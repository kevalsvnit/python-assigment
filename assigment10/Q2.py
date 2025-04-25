# 3. A magic square is an N×N grid of numbers in which the entries in each row,
#    column and main diagonal sum to the same number (equal to N(N^2+1)/2).
#    Create a magic square for N = 4, 5, 6, 7, 8

import numpy as np

# Function to generate a magic square for odd N (like 5, 7)
def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2  # Start in the middle of the first row

    for num in range(1, n*n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n  # Move up and right
        if magic_square[new_i, new_j]:  # If already filled, move down instead
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic_square

# Function for doubly even N (like 4, 8)
def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n*n + 1).reshape(n, n)
    # Flip certain positions
    indices = [(i, j) for i in range(n) for j in range(n)
               if (i % 4 == j % 4) or ((i + j) % 4 == 3)]
    for i, j in indices:
        magic_square[i, j] = n*n + 1 - magic_square[i, j]
    return magic_square

# Function for singly even N (like 6)
def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square = generate_odd_magic_square(half_n)

    magic_square = np.zeros((n, n), dtype=int)
    add = [0, 2 * half_n**2, 3 * half_n**2, half_n**2]  # Offsets for 4 blocks

    for r in range(half_n):
        for c in range(half_n):
            for k in range(4):
                i = r + (k // 2) * half_n
                j = c + (k % 2) * half_n
                magic_square[i][j] = sub_square[r][c] + add[k]

    # Swap specific columns
    n_cols = half_n // 2
    for i in range(half_n):
        for j in range(n_cols):
            if j == n_cols - 1 and i == n_cols:
                continue
            magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
    for i in range(half_n):
        for j in range(n_cols + 1, half_n):
            magic_square[i, j + half_n], magic_square[i + half_n, j + half_n] = \
                magic_square[i + half_n, j + half_n], magic_square[i, j + half_n]

    return magic_square

# Master function to call correct generator
def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

# Print magic squares for N from 4 to 8
for N in range(4, 9):
    print(f"\nMagic Square (N = {N}):\n")
    print(generate_magic_square(N))
