
# Exercise 4.3: Calculating derivatives


# a)

import numpy as np
import matplotlib.pyplot as plt
import argparse


def f(x):
    return x * (x - 1)

def derivative(f, x, delta=1e-2):
    return (f(x + delta) - f(x)) / delta

# Loop over a range of x values
for x in range(1, 11):
    # Calculate the derivative at x using the numerical method
    numerical_derivative = derivative(f, x)

    # Calculate the true derivative analytically
    true_derivative = 2 * x - 1

    print(f'At x = {x}:')
    print(f'Numerical derivative: {numerical_derivative}')
    print(f'True derivative: {true_derivative}')
    print(f'Difference: {abs(numerical_derivative - true_derivative)}\n')


# b)

deltas = [10**-i for i in range(2, 15, 2)]

# Initialize a list to store the differences
differences = []

# Loop over the delta values
for delta in deltas:
    # Calculate the derivative at x using the numerical method
    numerical_derivative = derivative(f, x, delta)

    # Calculate the true derivative analytically
    true_derivative = 2 * x - 1

    # Calculate the difference and add it to the list
    difference = abs(numerical_derivative - true_derivative)
    differences.append(difference)


# Plot the differences as a function of delta
plt.loglog(deltas, differences, 'o-')
plt.xlim(1e-16, 1e-0)
plt.xlabel('Delta')
plt.ylabel('Difference')
plt.title('Calculating Derivative')
plt.show()