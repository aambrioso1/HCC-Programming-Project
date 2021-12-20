# walker.py
# -----------------------------------------------------------------------------
# Make a movie out of the steps of a two-dimensional random walk.
# ----------------------------------------------------------------------------- 
"""
This code is from:  A Student's Guide to Python for Physical Modeling
by Jesse M. Kinder and Philip Nelson

The book can be purchased from Princeton Press here:
https://press.princeton.edu/books/paperback/9780691223650/a-students-guide-to-python-for-physical-modeling
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import random as rand

# Set number of steps for each random walk.
num_steps = 100

# Create an empty figure of the desired size.
bound = 20
fig = plt.figure() 		# must have figure object for movie
ax = plt.axes(xlim=(-bound, bound), ylim=(-bound, bound))
ax.set_aspect('equal')  # equal scaling for x and y axes

# Create a line and a point with no data.  They will be updated during each
# frame of the animation.
(my_line,) = ax.plot([], [], lw=2)				# line to show path
(my_point,) = ax.plot([], [], 'ro', ms=9)		# dot to show current position

# Generate the random walk data.
x_steps = 2*(rand(num_steps) < 0.5) - 1		# generate random steps +/- 1
y_steps = 2*(rand(num_steps) < 0.5) - 1
x_coordinate = x_steps.cumsum()				# sum steps to get position
y_coordinate = y_steps.cumsum()

# This function will generate each frame of the animation.
# It adds all of the data through frame n to a line
# and moves a point to the nth position of the walk.
def get_step(n, x, y, this_line, this_point):
	this_line.set_data(x[:n+1], y[:n+1])
	this_point.set_data(x[n], y[n])

# Call the animator and create the movie.
my_movie = animation.FuncAnimation(fig, get_step, frames=num_steps, \
					fargs=(x_coordinate,y_coordinate,my_line,my_point) )

# Save the movie in the current directory.
# *** THIS WILL CAUSE AN ERROR UNLESS FFMPEG OR MENCODER IS INSTALLED. ***
my_movie.save('random_walk.mp4', fps=30)