
# Exercise 8.4: Motion of a Nonlinear Pendulum

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Given constants
g = 9.81 
l = 0.1
theta0 = np.radians(179) 
omega0 = 0

# Function defining the differential equations
def pendulum_motion(t, y):
    theta, omega = y[0], y[1]
    dtheta_dt = omega
    domega_dt = -g / l * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Runge-Kutta method for solving the differential equations
def runge_kutta_step(t, y, dt):
    k1 = dt * np.array(pendulum_motion(t, y))
    k2 = dt * np.array(pendulum_motion(t + 0.5 * dt, y + 0.5 * k1))
    k3 = dt * np.array(pendulum_motion(t + 0.5 * dt, y + 0.5 * k2))
    k4 = dt * np.array(pendulum_motion(t + dt, y + k3))
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Time parameters (in seconds)
t_max = 10
dt = 0.01

# Initial conditions
initial_conditions = [theta0, omega0]

# Initialize arrays to store results
t_values = np.arange(0, t_max, dt)
theta_values = np.zeros_like(t_values)
omega_values = np.zeros_like(t_values)

# Perform Runge-Kutta integration
y = initial_conditions
for i, t in enumerate(t_values):
    theta_values[i] = y[0]
    omega_values[i] = y[1]
    y = runge_kutta_step(t, y, dt)

# Plotting the angle as a function of time
plt.figure(figsize=(8, 6))
plt.plot(t_values, np.degrees(theta_values))
plt.title('Angle vs Time for Nonlinear Pendulum')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.grid(True)
plt.show()

# Animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-l, l)
ax.set_ylim(-l, l)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Motion of a Nonlinear Pendulum')
line, = ax.plot([], [], 'o-', lw=1)

def animate(i):
    angle = theta_values[i]
    x = [0, l * np.sin(angle)]
    y = [0, -l * np.cos(angle)]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=len(t_values), blit=True, interval=20)
plt.show()
