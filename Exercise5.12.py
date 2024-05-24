
# Exercise 5.12: The Stefan–Boltzmann constant

import numpy as np
import scipy.integrate as integrate
# Import the constants from astropy
from astropy.constants import k_B, c, hbar, sigma_sb


# Define the integrand function
def integrand(x):
    return x**3 / (np.exp(x) - 1)

# Evaluate the integral
result, error = integrate.quad(integrand, 0, np.inf)    # Integrate from 0 to infinity
print(f"The integral evaluates to: {result:.10f} with an error estimate of {error:.10f}")

# Constants in SI units
k_B_value = k_B.value  # Boltzmann constant in J/K
c_value = c.value  # Speed of light in m/s
hbar_value = hbar.value  # Reduced Planck's constant in J·s


# Compare values of the Stefan Boltzmann constant: Calculated value vs. Known value
# Calculated values
sigma_calculated = (k_B_value**4 * result) / (4 * np.pi**2 * c_value**2 * hbar_value**3)
print(f"Computed Stefan–Boltzmann constant: {sigma_calculated:.10e} W/m^2K^4")
# Known values
sigma_known = sigma_sb.value  # W/m^2K^4
print(f"Known Stefan–Boltzmann constant: {sigma_known:.10e} W/m^2K^4")


# Compare the results
difference = abs(sigma_calculated - sigma_known)
print(f"Difference: {difference:.10e} W/m^2K^4")
