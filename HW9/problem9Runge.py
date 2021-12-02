import numpy as np, matplotlib as mpl, matplotlib.pyplot as plt, os, matplotlib.patches as mpl_patches
# if os.getcwd()[-1] != "HW9":
#     os.chdir("HW9")
"""
I use a 4th-order Runge_Kutta approximation for r dot, and a second-order Taylor approximation for r

rii = r double dot
ri = r dot
ri_0 = intital r dot
r_0 = initial r
"""

def rii(r):
    if r == 0:
        print("r is 0")
        return 0
    centrifugal = l2 / (mu*mu * r**3)
    accel = - U0*np.exp(-r/r0) / (mu * r) * (1 + 1/r)
    #accel = -U0*r0/r**2 / mu # if inverse square force instead
    return centrifugal + accel

r0 = 1.
U0 = 1.
mu = 1.
l2 = .5
l = .5**.5
###
ri_0 = .5
r_0 = 1
###

final_time = 100
dt = 0.001

t = 0

r_array = np.zeros(len(range(int(final_time/dt))))
ri_array = np.zeros(len(range(int(final_time/dt))))
times = np.zeros(len(range(int(final_time/dt))))
phi = np.zeros(len(range(int(final_time/dt))))

phi[0] = 0
times[0] = t
ri_array[0] = ri_0
r_array[0] = r_0
ri = ri_0

####### this the simulation
for i in range(1, int(final_time/dt)):
    r = r_array[i-1] # current r before adding another one
    r_array[i] = r + dt*ri + .5*dt*dt*rii(r) # second order Taylor aprox because I am unsure how to incorporate a Runge-Kutta here
    t += dt
    times[i] = t

    phi[i] = phi[i-1] + dt * l / (mu * r**2)

    #update ri using new r
    r = r_array[i]
    k1 = dt*rii(r)
    k2 = dt*rii(r+.5*k1)
    k3 = dt*rii(r+.5*k2)
    k4 = dt*rii(r+k3)
    ri = ri + 1/6*k1 + 1/3*k2 + 1/3*k3 + 1/6*k4 # fourth order Runge-Kutta
    #ri = ri + dt*rii(r)
    ri_array[i] = ri
#######
start = 0#90000
stop = 1e9
stop = min(stop, len(times))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (7,7))
ax1.plot(times[start:stop], r_array[start:stop], 'o')
ax1.set_ylabel('r')
ax1.set_title("r & dr/dt vs time")

labels = []
labels.append("r(t=0) = {}".format(r_0)) # these give the textbox in the upper right
labels.append("dr/dt(t=0) = {}".format(ri_0))
handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", alpha=0)] * len(labels)
ax1.legend(handles, labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)


ax2.plot(times[start:stop], ri_array[start:stop], 'o')
ax2.set_ylabel("dr/dt")

ax2.set_xlabel("time")

# print("# r array")
# print(r_array)
# print("#")

# print(ri_array)
# print("#")

plt.savefig("hw9_runge.pdf")
plt.show()

x = r_array * np.cos(phi)
y = r_array * np.sin(phi)
plt.plot(x[start:stop],y[start:stop])
plt.plot(x[0], y[0], 'ro', label = "t = 0")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Particle Position")

labels = []
labels.append("r(t=0) = {}".format(r_0)) # these give the textbox in the upper right
labels.append("dr/dt(t=0) = {}".format(ri_0))
handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", alpha=0)] * len(labels)
plt.legend(handles, labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)


#plt.legend()
plt.show()

print(len(times))