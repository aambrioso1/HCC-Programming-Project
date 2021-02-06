# A visual demo of Monte Carlo technique for calculating Pi.

import matplotlib.pyplot as plt
from random import random

# The number of points
n = 10

# Initialize lists for the coordinates
b_x = []
b_y = []
r_x = []
r_y = []


# Initialize counter for red points
r_count = 0

for i in range(n):
    # Generate n random points
    x = random()
    y = random()

    # Decide if points are inside circle
    c = x ** 2 + y ** 2
    if c > 1:
        # Add points outside of the circle to the blue list
        b_x.append(x)
        b_y.append(y)
    else:
        # Add points inside of the circle to the red list
        r_x.append(x)
        r_y.append(y)
        
        # Increment the count of red points
        r_count += 1

print(f'b_x = {b_x}')
print(f'b_y = {b_y}')
print(f'r_x = {r_x}')
print(f'r_x = {r_y}')

# Use the fraction of red points to to compute Pi
print(f'Pi is about {(4.0 * r_count) / n}')

# Plot the red and blue points together

# The two pairs of numbers give the maximum minumun on the graph for x and y.
plt.axis([0, 1, 0, 1])

# Scales the axes equally so the circle does not look like an ellipse.
plt.axis('equal')

# Plot the blue points
plt.plot(b_x, b_y, 'bo')

# Plot the red points
plt.plot(r_x, r_y, 'ro')


# Save the plot in the current working directory with a nice filename. Commented out for now.  
#  See https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig

# filename = 'pi_'+ str(n) + '.png' # Constructed so that file name includes the number of points
# plt.savefig('pi_'+ str(n) + '.png')

# Display the plot 
plt.show()


