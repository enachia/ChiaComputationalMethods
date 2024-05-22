import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_steps = 100  # Number of steps in each simulation
num_simulations = 1000  # Number of simulations for Monte Carlo

# Function to perform a random walk
def random_walk(num_steps):
    x, y = [0], [0]  # Starting point
    for _ in range(num_steps):
        angle = np.random.uniform(0, 2*np.pi)
        x.append(x[-1] + np.cos(angle))
        y.append(y[-1] + np.sin(angle))
    return x, y

# Perform simulation
end_positions = []
for _ in range(num_simulations):
    x, y = random_walk(num_steps)
    end_positions.append((x[-1], y[-1]))

# Convert to numpy array 
end_positions = np.array(end_positions)

# Analyze the distribution of end positions
mean_x, mean_y = np.mean(end_positions, axis=0)
std_x, std_y = np.std(end_positions, axis=0)

print(f"Mean end position: ({mean_x}, {mean_y})")
print(f"Standard deviation of end positions: ({std_x}, {std_y})")

# Plotting a sample random walk and the distribution of end positions
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Sample random walk
x, y = random_walk(num_steps)
ax[0].plot(x, y, marker='o')
ax[0].set_title('Sample Random Walk')
ax[0].set_xlim(min(x) - 1, max(x) + 1)
ax[0].set_ylim(min(y) - 1, max(y) + 1)

# Distribution of end positions
ax[1].scatter(end_positions[:, 0], end_positions[:, 1], alpha=0.6)
ax[1].set_title('Distribution of End Positions')
ax[1].set_xlim(np.min(end_positions[:, 0]) - 1, np.max(end_positions[:, 0]) + 1)
ax[1].set_ylim(np.min(end_positions[:, 1]) - 1, np.max(end_positions[:, 1]) + 1)

plt.show()

# Create an animated GIF of a sample random walk
fig, ax = plt.subplots()
ax.set_xlim(min(x) - 1, max(x) + 1)
ax.set_ylim(min(y) - 1, max(y) + 1)
line, = ax.plot([], [], color='pink')

particle = plt.Circle((0, 0), radius=0.075, fc='r')
ax.add_patch(particle)

def animate(i):
    position = particle.center
    x = plt.set_xlim(min(x) - 1, max(x) + 1)
    y = ax.set_ylim(min(y) - 1, max(y) + 1)
    line, = ax.plot([], [], color='pink')

#def init():
    #line.set_data([], [])
    #return line,


ani = FuncAnimation(fig, animate, frames=range(1, num_steps + 1), blit=True)

plt.show()
