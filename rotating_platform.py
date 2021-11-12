# rotating_platform.py 

# Implements a platform that allows for animating yaw, pitch, and roll
# and roll simultaneous in different proportions.   The variables
# yaw_factor, pitch_factor, and roll_factor control the proportions.
# Adjust this factors and explore the behavior of the platform.

# Base on code found here:
# https://toptechboy.com/9-axis-imu-lesson-21-visualizing-3d-rotations-in-vpython-using-quaternions/
# by Paul McWhorter 

# Best derivation I found for Rodriques Rotation Formula:
# https://mathworld.wolfram.com/RotationFormula.html

from vpython import *
from time import *
import numpy as np
import math
# import serial
# ad=serial.Serial('com5',115200)
 
scene.range=5
scene.background=color.white
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)
 
scene.width=600
scene.height=600
 
xarrow=arrow(length=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(length=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(length=2, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))

# scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
# scene.forward=vector(-1,-1,-1)

bBoard=box(length=6,width=2,height=.2,opacity=0.8,pos=vector(0,0,0))
myObj = compound([bBoard])

DEG = 15 # Use for static pitch
y = vector(0,1,0)

# These variables control the rate of yaw, pitch, and roll
# Try varying these proportions

yaw_factor = 1
pitch_factor = 1/5
roll_factor = 10

while(True):
    # pitch = DEG * toRad # use for static pitch
    # roll = DEG * toRad # use for static roll

    for angle in np.arange(0, 12*np.pi, 0.01):
        
        yaw = angle * yaw_factor
        pitch = angle * pitch_factor
        roll = angle * roll_factor
        
        rate(100)
        
        # forward vector
        k = vector(cos(yaw)*cos(pitch), sin(pitch), sin(yaw)*cos(pitch))

        # side vector
        s = cross(k,y)

        # up vector
        v = cross(s,k)

        # Rodriques rotation formula included here
        # Note the McWhorter leave of the last term in his tutorial
        vrot=v*cos(roll) + cross(k,v)*sin(roll) + k*dot(k,v)*(1-cos(roll))

        frontArrow.axis = k
        frontArrow.length = 4
        sideArrow.axis = cross(k,vrot)
        sideArrow.length = 2
        upArrow.axis = vrot
        upArrow.length = 1

        myObj.axis = k
        myObj.up = vrot

sleep(60)

""" 
frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))


bBoard=box(length=6,width=2,height=.2,opacity=0.2,pos=vector(0,0,0,))
bn=box(length=1,width=.75,height=.1, pos=vector(-.5,.1+.05,0),color=color.blue)
nano=box(lenght=1.75,width=.6,height=.1,pos=vector(-2,.1+.05,0),color=color.green)
myObj=compound([bBoard,bn,nano])
while (True):
    try:
        while (ad.inWaiting()==0):
            pass
        dataPacket=ad.readline()
        dataPacket=str(dataPacket,'utf-8')
        splitPacket=dataPacket.split(",")
        q0=float(splitPacket[0])
        q1=float(splitPacket[1])
        q2=float(splitPacket[2])
        q3=float(splitPacket[3])
 
        roll=-math.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
        pitch=math.asin(2*(q0*q2-q3*q1))
        yaw=-math.atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))-np.pi/2
 
        rate(50)
        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll)+cross(k,v)*sin(roll)
 
        frontArrow.axis=k
        sideArrow.axis=cross(k,vrot)
        upArrow.axis=vrot
        myObj.axis=k
        myObj.up=vrot
        sideArrow.length=2
        frontArrow.length=4
        upArrow.length=1
    except:
        pass
"""