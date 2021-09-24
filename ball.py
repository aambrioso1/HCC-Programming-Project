# ball.py

# For documentation on vpython:
# https://vpython.org/
# https://www.glowscript.org/docs/VPythonDocs/VPython_Intro.pdf
from vpython import *  # Import the vpython module

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.red)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.blue)
wallT = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.orange)
wallB = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.yellow)

ball.velocity = vector(25,5,0)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity*deltat
while t < 10:
	# The rate determines that maximum number of times per second
	# that while loop will be executed
	rate(100)

	# The conditionls reverse the ball when it hits a wall
	if ball.pos.x + 0.5 > wallR.pos.x or ball.pos.x < wallL.pos.x:
		ball.velocity.x = -ball.velocity.x
	if ball.pos.y > wallT.pos.y or ball.pos.y < wallB.pos.y:
		ball.velocity.y = -ball.velocity.y
	
	# We update the ball's position
	ball.pos = ball.pos + ball.velocity*deltat
	t = t + deltat
