# rotating_line.py

import numpy as np
import math
import matplotlib.pyplot as plt

from matplotlib import animation
from numpy.random import random as rand

def rotate_clockwise(vector, theta):
	"""
	Creates a new vector by rotating vector theta radians clockwise.
	"""
	clock_matrix = np.array([[math.cos(theta), math.sin(theta)],
              [(-1) * math.sin(theta), math.cos(theta)]])
	rotated_vector = np.matmul(clock_matrix, vector)
	return rotated_vector

def rotate_counterclockwise(vector, theta):
	"""
	Creates a new vector by rotating vector theta radians clockwise.
	"""
	counter_matrix = np.array([[math.cos(theta), (-1) * math.sin(theta)],
              [math.sin(theta), math.cos(theta)]])
	rotated_vector = np.matmul(counter_matrix, vector)
	return rotated_vector

"""
Creates an animation that illustrates rotation by matrix multiplication
The animation is stored in a file called "rotating_line.mp4.

The code follows an example found in the follow book:
See pp. 99-100 of "A Student's Guide to Python for Physical Modeling."
"""

# Set number of steps
num_steps = 96

# Create an empty figure of the desired size.
bound = 20
fig = plt.figure() 		# must have figure object for movie
ax = plt.axes(xlim=(-bound, bound), ylim=(-bound, bound))
ax.set_aspect('equal')  # equal scaling for x and y axes

# Create a line and a point with no data.  They will be updated during each
# frame of the animation.
(my_line,) = ax.plot([], [], lw=1)				# line to show path

x_coordinates = np.array([0,10])
y_coordinates = np.array([0,0])


line_vector = np.array([10,0])

for _ in range(48):
	line_vector = rotate_counterclockwise(line_vector, np.pi/24)
	x_coordinates = np.append(x_coordinates, 0)
	x_coordinates = np.append(x_coordinates, line_vector[0])
	y_coordinates = np.append(y_coordinates, 0)
	y_coordinates = np.append(y_coordinates, line_vector[1])
	

def get_step(n, x, y, this_line):
	this_line.set_data(x[:n+1], y[:n+1])

# Call the animator and create the movie.
my_movie = animation.FuncAnimation(fig, get_step, frames=num_steps, \
					fargs=(x_coordinates,y_coordinates,my_line) )

# Save the movie in the current directory.
# *** THIS WILL CAUSE AN ERROR UNLESS FFMPEG OR MENCODER IS INSTALLED. ***
my_movie.save('rotating_line.mp4', fps=5)

