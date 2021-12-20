# rotating_line_segments.py

"""


For information on the connection between the matrices and the trigonometry
involved in the rotations see "Examples in 2 dimensions" in this article:
https://en.wikipedia.org/wiki/Transformation_matrix
"""

"""
For computing the angle between two vectors in numpy.
https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python

For handling special cases when angles are parallel
https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python/13849249#13849249
"""

import numpy as np
import numpy.linalg as LA
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

def find_angle(v1, v2):
	"""computes the angle between two vectors
	args: v1 and v2 - two numpy arrays
	output: rad, deg - radian and degree measure of the angle
	vectors
	"""
	inner = np.inner(v1, v2)
	norms = LA.norm(v1) * LA.norm(v2)

	cos = inner / norms
	rad = np.arccos(np.clip(cos, -1.0, 1.0))
	deg = np.rad2deg(rad)
	return rad, deg

def unit_vector(v):
	"""returns the unit vector in the direction of v
	"""
	return v / LA.norm(v)

def find_vector(vector, theta, l):
	"""Finds a new vector of length by rotating v1 clockwise
	a scaling the vector to L
	""" 
	new_v = rotate_clockwise(vector,theta)
	new_dir = new_v/LA.norm(new_v)
	return l * new_dir

theta = 2 * np.pi/3 # direction of orginal vector
h = 5 # length of original vector

theta_rot = np.pi/3 # angle that orginal vector is rotated clockwise
l = 1.5 # length of new vector

v0 = h * np.array([np.cos(theta), np.sin(theta)]) 
x0 = v0[0]
y0 = v0[1]

v1 = find_vector(v0, theta_rot, l) # new vector
x1 = v1[0]
y1 = v1[1]

print(f"P2 is ({x1},{y1})")

fig = plt.figure() # create a plot
ax = fig.add_subplot(111) # place plot in fig

# Plot the original vector and the rotated vector
plt.plot([0, x0],[0,y0]) 
plt.plot([0, x1],[0,y1])

plt.axis([-5,5,-5,5]) # Determine the range of the x and y axes.
plt.grid(True) # Add grid lines
ax.set_aspect('equal', adjustable='box') # Scales the axis the same
plt.show() # Outputs the plot


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
"""
# This function will generate each frame of the animation.
# It adds all of the data through frame n to a line
# and moves a point to the nth position of the walk.
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
"""
