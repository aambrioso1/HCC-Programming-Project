# A visual demo of Monte Carlo technique for calculating Pi.

import matplotlib.pyplot as plt
from random import random

# The number of points
n = 1000

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


# Use the fraction of red points to to compute Pi
print(f'Pi is about {(4.0 * r_count) / n}')

# Plot the red and blue points together
plt.axis([0, 1, 0, 1])
# Scales the axes equally so the circle does not # look like an ellipse.
plt.axis('equal')

# Plot the blue points
plt.plot(b_x, b_y, 'ro')

# Plot the red points
plt.plot(r_x, r_y, 'go')

# Display the plot 
plt.show()
