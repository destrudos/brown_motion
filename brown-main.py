#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Dominik
# Created Date: 05.30.2023  0:15 CET
# version ='1.0'
# ---------------------------------------------------------------------------
""" Simple Brown motion simulation with numpy & matplotlib with track history"""
# ---------------------------------------------------------------------------
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting the window size
fig, ax = plt.subplots(figsize=(8,6))

# Simulation parameters
num_particles = 13
x_size = 800
y_size = 600
x = np.random.uniform(0, x_size, num_particles)
y = np.random.uniform(0, y_size, num_particles)
speed = 5  # Particle speed
radius = 10  # Particle radius

# Creating points on the plot
colors = np.random.rand(num_particles, 3)  # Random colors for each particle
points = ax.scatter(x, y, s=radius*10, c=colors)

# Creating lines for particle trails
trails = [ax.plot([], [], color=colors[i])[0] for i in range(num_particles)]

# Setting the axes to match the dimensions of the area
ax.set_xlim(0, x_size)
ax.set_ylim(0, y_size)

# Initializing history of positions for the trails
history_x = [list() for _ in range(num_particles)]
history_y = [list() for _ in range(num_particles)]

# Function for checking collisions between particles
def check_collision(x1, y1, x2, y2, r):
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance < 2*r

# Function to update particle positions
def update(frame):
    global x, y, history_x, history_y

    # Random direction for each particle
    angles = np.random.uniform(0, 2*np.pi, num_particles)
    dx = speed * np.cos(angles)
    dy = speed * np.sin(angles)

    x_new = x + dx
    y_new = y + dy

    # Check for collision between particles
    for i in range(num_particles):
        for j in range(i+1, num_particles):
            if check_collision(x_new[i], y_new[i], x_new[j], y_new[j], radius):
                dx[i], dx[j] = dx[j], dx[i]
                dy[i], dy[j] = dy[j], dy[i]
                x_new = x + dx
                y_new = y + dy

    x = x_new
    y = y_new

    # Update position history
    for i in range(num_particles):
        history_x[i].append(x[i])
        history_y[i].append(y[i])

    # Check if particles have gone beyond the area - if so, bounce them back
    x = np.where((x<0) | (x>x_size), x - 2*dx , x)
    y = np.where((y<0) | (y>y_size), y - 2*dy , y)

    points.set_offsets(np.c_[x, y])

    # Update the trails
    for i in range(num_particles):
        trails[i].set_data(history_x[i], history_y[i])

    return [points, *trails]

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=range(10000), interval=20, blit=True)

plt.show()
