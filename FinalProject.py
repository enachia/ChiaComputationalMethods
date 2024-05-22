import os
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio    # Use imageio v2 for compatibility with imageio-ffmpeg
import seaborn as sns

# Function to perform the random walk
def drunkards_walk(steps=1000):
    # Have the drunkard start at the origin
    x = [0]
    y = [0]
    
    for _ in range(steps):
        direction = np.random.choice(['up', 'down', 'left', 'right'])
        
        if direction == 'up':
            x.append(x[-1])
            y.append(y[-1] + 1)
        elif direction == 'down':
            x.append(x[-1])
            y.append(y[-1] - 1)
        elif direction == 'left':
            x.append(x[-1] - 1)
            y.append(y[-1])
        elif direction == 'right':
            x.append(x[-1] + 1)
            y.append(y[-1])
            
    return x, y

# Generate frames and save as images
def create_frames(steps=1000, interval=20):
    x, y = drunkards_walk(steps)
    filenames = [] # Store the filenames of the saved images

     # Start from interval to avoid empty sequence
    for i in range(interval, steps + 1, interval): 
        plt.figure(figsize=(6, 6))
        plt.plot(x[:i], y[:i], marker='o', color='violet', markersize=2, 
                 linewidth=0.75, alpha=0.5)
        plt.rcParams['axes.facecolor'] = 'silver' # Change background color
        
        # Set limits for x-axis and y-axis
        plt.xlim(-25, 25) 
        plt.ylim(-25, 25)
        
        plt.title(f'Drunkard\'s Walk: Step {i}')
        filename = f'walk_{i}.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()
        
    return filenames, x, y

# Create GIF from the saved frames
def create_gif(filenames, gif_name='drunkards_walk.gif'):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(gif_name, images, duration=0.2)
    
    # Clean up the image files
    for filename in filenames:
        os.remove(filename)

# Generate plot density
def plot_density(x, y):
    plt.figure(figsize=(8, 6))
    sns.kdeplot(x=x, y=y, cmap="RdPu", bw_adjust=0.5, cbar=True, fill=True)
    
    # Set limits for x-axis and y-axis
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)

    plt.title('Density Plot of Drunkard\'s Walk')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    density_plot_filename = 'density_plot.png'
    plt.savefig(density_plot_filename)
    plt.close()

# Plot positions vs. steps
def plot_positions_vs_steps(x, y):
    steps = range(len(x)) # Number of steps taken
    plt.figure(figsize=(10, 6))
    plt.plot(steps, x, label='X Position')
    plt.plot(steps, y, label='Y Position')
    plt.plot(steps)
    plt.xlabel('Steps')
    plt.ylabel('Position')
    plt.title('Position vs. Steps')
    plt.legend()
    positions_vs_steps_filename = 'positions_vs_steps.png'
    plt.savefig(positions_vs_steps_filename)
    plt.close()

# Generate the frames
filenames, x, y = create_frames(steps=1000, interval=10)

# Create the GIF
create_gif(filenames)

# Create the density plot
plot_density(x, y)

# Create the position vs. steps plot
plot_positions_vs_steps(x, y)