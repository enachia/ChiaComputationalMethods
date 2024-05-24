
# Exercise 4.4: Calculating integrals

import math
import numpy as np
import time


start = time.time()

# Given the function to integrate
def y_k(k, h):
    x_k = -1 + (h * k)
    return np.sqrt( 1 - ((x_k) ** 2) )

# Riemann sum
def riemann(f, n, a, b):
    n = 100 # Number of slices
    h = (b - a) / n # Width of each slice
    return sum(h * f(k, h) for k in range(1, n))

# Calculate the integral
r = riemann(y_k, 100, -1, 1)

end = time.time()

print(f"Integral is: {r}")
print(f"The Program took {end-start} seconds to run")