
# Exercise 10.8: Calculate a value for the integral

import numpy as np

# Define the integrand function
def integrand(x):
    return x**(-1/2) / (np.exp(x) + 1)

# Define the probability distribution function p(x)
def p(x):
    return 1 / (2 * np.sqrt(x))

# Number of random points
N = 1000000

# Generate random points from the distribution p(x)
u = np.random.rand(N)
x = u**2

# Evaluate the integrand at the sampled points
integrand_values = integrand(x)

# Evaluate the importance sampling formula
I_approx = np.mean(integrand_values / p(x))

print("Approximated integral value:", I_approx)