import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math
n = 8               # Number of particles
m = np.ones(n).astype(float)      # Particle masses
x = np.zeros((n,2)).astype(float) # Particle positions (x and y for ith particle in x[i,0], x[i,1])
v = np.zeros((n,2)).astype(float) # Particle velocities
f = np.zeros((n,2)).astype(float) # Force accumulator
dt = 0.02           # Time step

g = np.array([0,-9.8]) # Acceleration due to gravity

# Initialize
for i in range(n):
    m[i] = 1
    x[i,:] = np.array([0,0])
    v[i,:] = np.array([1,3.5])


# Time stepping (this is actually "semi-implicit Euler")
def step1():
    # Accumulate forces on each particle
    f.fill(0)
    for i in range(n):
        f[i,:] = m[i]*g
    # Update velocity of each particle
    for i in range(n):
        v[i,:] += f[i,:]/m[i] * dt
    # Update position of each particle
    for i in range(n):
        x[i,:] += v[i,:] * dt


def step2():
    f.fill(0)
    for i in range(n):
        f[i,:] = m[i]*g
    v0 = np.array([0.7,0.7])
    v1 = np.array([1,0])
    v2 = np.array([0.7,-0.7])
    v3 = np.array([0,1])
    v4 = np.array([0,-1])
    v5 = np.array([-0.7,0.7])
    v6 = np.array([-1,0])
    v7 = np.array([-0.7,-0.7])
    v[0]+=v0
    v[1]+=v1
    v[2]+=v2
    v[3]+=v3
    v[4]+=v4
    v[5]+=v5
    v[6]+=v6
    v[7]+=v7

    #for i in range(n):
     #   v[i,:] += f[i,:]/m[i] * dt
    for i in range(n):
        x[i,:] += v[i,:] * dt


# Drawing code
fig, ax = plt.subplots()
points, = ax.plot(x[:,0], x[:,1], 'o')

def init():
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal')
    return points,

def animate(frame):
    if frame == frames//3:
        step2()
    else:
        step1()

    points.set_data(x[:,0], x[:,1])
    if frame is frames-1:
        plt.close()
    return points,

totalTime = 1
frames = int(totalTime/dt)
anim = FuncAnimation(fig, animate, frames=range(frames), init_func=init, interval=dt*1000)
plt.show()
