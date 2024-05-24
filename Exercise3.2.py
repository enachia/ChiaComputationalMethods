import numpy as np
import matplotlib.pyplot as plt

# Function to plot the deltoid curve
def deltoid_curve(ax):
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)
    ax.plot(x, y, label='Deltoid Curve')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Deltoid Curve')
    ax.grid(True)
    ax.axis('equal')
    ax.legend()

# Function to plot the Galilean spiral
def galilean_spiral(ax):
    theta = np.linspace(0, 10 * np.pi, 1000)
    r = theta**2
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, label='Galilean Spiral')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Galilean Spiral')
    ax.grid(True)
    ax.axis('equal')
    ax.legend()

# Function to plot Fey's function
def feys_function(ax):
    theta = np.linspace(0, 24 * np.pi, 1000)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 12)**5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, label="Fey's Function")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Fey's Function")
    ax.grid(True)
    ax.axis('equal')
    ax.legend()

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(21, 7), tight_layout=True)
plt.suptitle('Parametric Curves', fontsize=16)

# List of plotting functions
plotting_functions = [deltoid_curve, galilean_spiral, feys_function]

# Loop through each plotting function and axis, and generate the plots
for ax, plot_func in zip(axes, plotting_functions):
    plot_func(ax)

# Show the plots
plt.show()
