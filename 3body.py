import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math

m1 = 40000
m2 = 40000
m3 = 40000

g = 100

pos = np.zeros((3, 2))
vel = np.zeros((3, 2))
dt = 0.02

pos[0,:] = np.array([0,0])
pos[1,:] = np.array([100,0])
pos[2,:] = np.array([50,50*1.7320508075688772])

poscentr = pos[0,:] + pos[1,:] + pos[2,:]
poscentr /= 3
for i in range(3):
	pos[i,:] -= poscentr

vel[0,:] = 2*4.5*5*np.array([-5,0])
vel[2,:] = 2*4.5*5*np.array([5/2,1*1.7320508075688772/2*5])
vel[1,:] = 2*4.5*5*np.array([1/2*5,-1*1.7320508075688772/2*5])

def r(x, y, z):
	return sqrt(x*x + y*y + z*z)

def f(M, x0, y0, m1, x1, y1, m2, x2, y2):
	v1 = np.array([x1-x0,y1-y0])
	v2 = np.array([x2-x0,y2-y0])
	r1 = math.sqrt((x1-x0)**2 + (y1-y0)**2)
	r2 = math.sqrt((x2-x0)**2 + (y2-y0)**2)
	force = g*(  m1/r1**3 * v1 + m2/r2**3 * v2   )
	return force

def step():

	f1 = f(m1, pos[0,0], pos[0,1], m2, pos[1,0], pos[1,1], m3, pos[2,0], pos[2,1])
	f2 = f(m2, pos[1,0], pos[1,1], m3, pos[2,0], pos[2,1], m1, pos[0,0], pos[0,1])
	f3 = f(m3, pos[2,0], pos[2,1], m1, pos[0,0], pos[0,1], m2, pos[1,0], pos[1,1])

	vel[0,:] += f1*dt
	vel[1,:] += f2*dt
	vel[2,:] += f3*dt

	for i in range(3):
		pos[i,:] += vel[i,:]*dt

# Drawing code
fig, ax = plt.subplots()
points, = ax.plot(pos[:,0], pos[:,1], 'o')

def init():
	ax.set_xlim(-300,300)
	ax.set_ylim(-300,300)
	ax.set_aspect('equal')
	return points,

def animate(frame):
	step()
	points.set_data(pos[:,0], pos[:,1])
	if frame is frames-1:
		plt.close()
	return points,

totalTime = 10
frames = int(totalTime/dt)
anim = FuncAnimation(fig, animate, frames=range(frames), init_func=init, interval=dt*1000)
plt.show()
