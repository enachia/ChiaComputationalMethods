
# Exercise 6.14: Nonlinear Equations

import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Planck's constant over 2*pi in J*s
eV = 1.60218e-19 # Conversion factor from eV to J
m = 9.1094e-31  # Mass of electron in kg
V = 20 * eV  # Potential in J (converted from eV)
w = 1e-9  # Width in meters


# Energy range
E_values = np.linspace(0, V, 1000)

# Calculate y1, y2, y3
y1 = np.tan(np.sqrt(w**2 * m * E_values / (2 * hbar**2)))
y2 = np.sqrt((V - E_values) / E_values)
y3 = -np.sqrt(E_values / (V - E_values))

# Plot the quantities
plt.plot(E_values / eV, y1, label=r'$\tan{\left(\sqrt{\frac{w^2 m E}{2 \hbar^2}}\right)}$')
plt.plot(E_values / eV, y2, label=r'$\sqrt{\frac{V-E}{E}}$')
plt.plot(E_values / eV, y3, label=r'$-\sqrt{\frac{E}{V-E}}$')
plt.xlabel('Energy (eV)')
plt.ylabel('Quantity')
plt.title('Functions of Energy')
plt.legend()
plt.grid(True)
plt.show()
