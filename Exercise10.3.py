
# Exercise 10.3: Brownian motion

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Position
x_pos = [0]
y_pos = [0]
frames = 1800



# Animation
fig, ax = plt.subplots(figsize=(6, 6)); ax.set_xlim(-50, 50); ax.set_ylim(-50, 50); ax.set_title('Brownian Motion')
# Particle
particle = plt.Circle((0, 0), 0.75, fc='c')
ax.add_patch(particle)
# Tracing
line = ax.plot(x_pos, y_pos, c='g', alpha=0.5)[0]
ax.set_aspect('equal')
ax.grid(True)



def animate(i):
     particle.center = (x_pos[-1], y_pos[-1]) # centering

     x_pos.append(x_pos[-1] + rand.normal())
     y_pos.append(y_pos[-1] + rand.normal())

     direction = rand.rand() * 360 # direction

     x_pos[-1] += np.cos(direction) # x position
     y_pos[-1] += np.sin(direction) # y position

     particle.set_facecolor((rand.rand(), rand.rand(), rand.rand())) # coloring

     #tracing (line)
     line.set_xdata(x_pos)
     line.set_ydata(y_pos)
     return particle,

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=10)
plt.show()