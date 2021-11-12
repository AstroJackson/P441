import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpl_patches

def alpha(phi, t):
  return -g/l*np.sin(phi) + R/l*w*w*(np.sin(w*t) * np.sin(phi) + np.cos(w*t) * np.cos(phi))
######## Feel free to edit these to change the simulation!
g = 9.8
R = 1.
l = 3
w = 2

frame_speed = 20 #edit this to change how many frames the simulation skips (somewhat related to fps (frames per second))
######## Nothing else needs to be edited


dt = .01 # determines how accurate the simulation is. A lower dt gives a more accurate simulation!
t = 0.
final_time = 10000
v = 0 # dphi / dt
p = [0.] # phi
times = [0] # list of times, in seconds

for i in range(int(final_time/dt)): # these few lines are the actual simulation, solving technique
  v += alpha(p[i], t)*dt # linear order Taylor series approximation
  p.append(p[i]+v*dt) # linear order TS aprox
  t += dt
  times.append(t)
p = np.array(p)
times = np.array(times)
wheel_x = R*np.cos(w*times)
wheel_y = -R*np.sin(w*times)

x_pos = R * np.cos(w*times) + l*np.sin(p)
y_pos = -R * np.sin(w*times) + l*np.cos(p)

# plt.plot(times, p)

# plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(8.5, 8.5)
xdata, ydata = [], []
#plt.text(-(R+l)-.95, -(R+l)-.8, f'$w = {w}$', fontsize = 11, bbox = dict(facecolor = 'yellow', alpha = 0.5))
labels = []
labels.append("w = {} rad/s".format(w)) # these give the textbox in the upper right
labels.append("L = {} m".format(l))
labels.append("R = {} m".format(R))
handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", alpha=0)] * len(labels)
ax.legend(handles, labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)
time_text = ax.text(-(R+l)-.95, (R+l)+.9,'') # this gives the time elapsed in the lower left

plt.plot(wheel_x, wheel_y) # plots the wheel that the pendulum is fixed to
plt.axis([-(R+l)-1, (R+l)+1, (R+l)+1, -(R+l)-1])
ln, = plt.plot([], []) # the pendulum rod will go here
pt1, = ax.plot([], [], 'g.', ms=20) # the location of the mass will go here

def init():
    time_text.set_text('initial') # initiates
    ax.set_xlim(-(R+l)-1, (R+l)+1)
    ax.set_ylim((R+l)+1, -(R+l)-1)
    return time_text, ln

def update(frame): # the animation part of this code
    xdata = [x_pos[frame], wheel_x[frame]] # the pendulum rod
    ydata = [y_pos[frame], wheel_y[frame]] # pendulum rod
    ln.set_data(xdata, ydata) # pendulum rod
    time_text.set_text(f'Time = {round(times[frame],1)} s') # time elapses updated
    pt1.set_data(x_pos[frame],y_pos[frame]) # mass position updated
    #plt.text(0,0, f'$w = {w+frame}$', fontsize = 11, bbox = dict(facecolor = 'yellow', alpha = 0.5))
    return time_text, ln, pt1
#plt.plot(wheel_x, wheel_y)
ani = FuncAnimation(fig, update, frames= range(0, 100000, 20),init_func=init, blit=True)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Pendulum on a Rotating Wheel")
plt.show()