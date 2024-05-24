
# Exercise 8.7: Trajectory with air resistance

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
R = 0.08 # Radius of the cannonball in meters
rho = 1.22  # Density of air in kg/m^3
C = 0.47  
m = 1.0  
g = 9.81  

# Initial conditions
v0 = 100  
theta = np.radians(30) 
v0x = v0 * np.cos(theta) 
v0y = v0 * np.sin(theta)  

# Function defining the differential equations
def cannonball_motion(t, y):
    vx, vy = y[2], y[3]  
    v = np.sqrt(vx**2 + vy**2)  # Total velocity
    Fx = -0.5 * np.pi * R**2 * rho * C * vx * v
    Fy = -0.5 * np.pi * R**2 * rho * C * vy * v - m * g
    ax = Fx / m
    ay = Fy / m
    return [vx, vy, ax, ay]

# Time
t_span = (0, 10)

# Initial conditions
initial_conditions = [0, 0, v0x, v0y]

solution = solve_ivp(cannonball_motion, t_span, initial_conditions, t_eval=np.linspace(0, 10, 1000))

# Extracting solution
x = solution.y[0]
y = solution.y[1]

# Plotting the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Trajectory of Cannonball(s)')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()

max_distance = np.max(solution.y[0])
print("Total distance traveled by the cannonball:", max_distance, "meters")
