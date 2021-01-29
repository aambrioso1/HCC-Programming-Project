"""
We take a text file containing points that draw a fish and use it to generate lists we can 
manipulate in Python.   Then we use matplot and numpy to draw the fish and apply
transformation to the point with matrix multiplication.
"""
import matplotlib.pyplot as plt
import numpy as np
import math

with open('fish_points.txt', 'r') as reader:
	line_list = []
	for line in reader.readlines():
		# print(line, end='')
		line_list.append(line)

x_s, y_s = [], []

for i in range(1,len(line_list)-5):
	# print(f'line_list[{i}] = {line_list[i]}')
	# print(float(line_list[i][4:10]))
	# print(float(line_list[i][14:20]))
	x_s.append(float(line_list[i][4:10]))
	y_s.append(float(line_list[i][14:20]))

# print(f'x_s = {x_s}, y_s = {y_s}')

pairs = list(zip(x_s, y_s))


points = []
for pair in pairs:
	points.append(np.array(pair))

"""
# Create the same list with a list comprehension
points = [np.array(pair) for pair in pairs]
"""

# We create the transformation matrices
theta = math.pi/4
sx = 3
sy = 1
k = 1/3
stretch = np.array([[sx, 0], [0, sy]]) # Stretch
rotate = np.array([[math.cos(theta),(-1) * math.sin(theta)],[math.sin(theta), math.cos(theta)]]) # rotate
shear = np.array([[1, k],[0, 1]]) # shear

"""
transformed_points = []
for point in points:
	transformed_points.append(np.matmul(shear,point))
"""
# We multiply every point by one of the transforms to create list of the transformed points
transformed_points = [np.matmul(shear,point) for point in points]


# Separate the x's and y's of the transformed point pairs
T_x_s, T_y_s = [], []
for pair in transformed_points:
	x, y = pair
	T_x_s.append(x)
	T_y_s.append(y)

# Plot the original points
plt.scatter(x_s, y_s, marker='o')

# Plot the transformed points
plt.scatter(T_x_s, T_y_s, marker='o')


plt.show()
