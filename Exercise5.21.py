
# 5.21: Electric field of a charge distribution:

import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854e-12  # Permittivity (F/m)
q1 = 1.0  # Charge 
q2 = -1.0  # Charge 
r1 = np.array([-0.05, 0])  # Position of charge q1 
r2 = np.array([0.05, 0])  # Position of charge q2 

# Create a grid of points in the xy-plane
x = np.linspace(-0.1, 0.1)  # 1 cm spaced points from -0.5 m to 0.5 m
y = np.linspace(-0.1, 0.1)
X, Y = np.meshgrid(x, y)
grid_points = np.array([X, Y])

# Function to calculate the distance from a charge
def distance(point, charge_position):
    return np.sqrt((point[0] - charge_position[0])**2 + (point[1] - charge_position[1])**2)

# Calculate the electric potential at each point on the grid
V = (q1 / (4 * np.pi * epsilon_0 * distance(grid_points, r1)) +
     q2 / (4 * np.pi * epsilon_0 * distance(grid_points, r2)))


# Finite difference method to compute the gradient
Ex, Ey = np.gradient(V, -1, 1)

# Create subplots with shared axes
fig, axs = plt.subplots(1, 2, figsize=(10, 5), tight_layout=True)

# Electric potential contour plot
contour_plot = axs[0].contourf(X, Y, V, 100, cmap='RdBu')
plt.suptitle('Electric Potential and Electric Field due to Two Charges', fontsize=14)
fig.colorbar(contour_plot, ax=axs[0], label='Electric Potential (V)')
axs[0].set_xlabel('x (m)')
axs[0].set_ylabel('y (m)')
axs[0].set_title('Electric Potential')

# Electric field quiver plot
quiver_plot = axs[1].quiver(X, Y, -Ex, -Ey, scale=1e12, color='purple', pivot='middle', alpha=0.7)
axs[1].set_xlabel('x (m)')
axs[1].set_ylabel('y (m)')
axs[1].set_title('Electric Field')

plt.show()
