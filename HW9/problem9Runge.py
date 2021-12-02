import numpy as np, matplotlib as mpl, matplotlib.pyplot as plt, os
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
    centrigal = l2 / (mu*mu * r**3)
    accel = - U0*np.exp(-r/r0) / (mu * r) * (1 + 1/r)
    return centrigal + accel

r0 = 1.
U0 = 1.
mu = 1.
l2 = .5
###
ri_0 = 100
r_0 = 1
###

final_time = 100
dt = 0.01

t = 0

r_array = np.zeros(len(range(int(final_time/dt))))
ri_array = np.zeros(len(range(int(final_time/dt))))
times = np.zeros(len(range(int(final_time/dt))))

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

    #update ri using new r
    r = r_array[i]
    k1 = dt*rii(r)
    k2 = dt*rii(r+.5*k1)
    k3 = dt*rii(r+.5*k2)
    k4 = dt*rii(r+k3)
    ri = 1/6*k1 + 1/3*k2 + 1/3*k3 + 1/6*k4 # fourth order Runge-Kutta
    #ri = ri + dt*rii(r)
    ri_array[i] = ri
#######

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(times, r_array, 'o')
ax1.set_ylabel('r')
ax1.set_title("r & dr/dt vs time (Runge-Kutta)")

ax2.plot(times, ri_array, 'o')
ax2.set_ylabel("dr/dt")

ax2.set_xlabel("time")

print(ri_array)

plt.savefig("hw9_runge.pdf")
plt.show()