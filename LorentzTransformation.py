import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button, RadioButtons
#Plots a Lorentz Transformation with velocity slider

#Creating the t array is not neccessary here but it is used for clarity.  
x = np.linspace(0, 10, 400)
t = np.linspace(0, 10, 400)
c = 1
v = .5
step_size = 2


def x_prime(v, n):

	x_prime = []

	for i in x:
		x_prime.append(v/c*i+n*step_size)

	return x_prime

def t_prime_2(v, n):

	result = []

	for i in t:
		#You have to divde by "v" in the step size because we want to tansform the t-axis which means we must transform x.  However, since t = x/v, if we want to add a constant,
		#say, "-a", we must add it as a/v therefore t = x/v - a/v = (x-a)/v which is translating to the right an "a" amount
		result.append(c/v*i-n*step_size/v)

	return result

fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

ax.set_title("Space and Time Under Lorentz Transformations")
ax.set_xlabel("x")
ax.set_ylabel("t")
fig.subplots_adjust(left=0.15, bottom=0.25)

#The Light Cone
ax.plot(x, x, color="black", linewidth=5.0)

#A reference frame goign 50% the speed of light
x_axis0, = ax.plot(x, x_prime(v, 0), color="blue", linewidth=5.0)
time_axis0,  = ax.plot(x, t_prime_2(v, 0), color="blue", linewidth=5.0)

#Setting up grid in the prime coordinates 
time_axis1, = ax.plot(x, t_prime_2(v, 1), color="blue", linestyle='--')
time_axis2, = ax.plot(x, t_prime_2(v, 2), color="blue", linestyle='--')
time_axis3, = ax.plot(x, t_prime_2(v, 3), color="blue", linestyle='--')
time_axis4, = ax.plot(x, t_prime_2(v, 4), color="blue", linestyle='--')

x_axis1, = ax.plot(x, x_prime(v, 1), color="blue", linestyle='--')
x_axis2, = ax.plot(x, x_prime(v, 2), color="blue", linestyle='--')
x_axis3, = ax.plot(x, x_prime(v, 3), color="blue", linestyle='--')
x_axis4, = ax.plot(x, x_prime(v, 4), color="blue", linestyle='--')

#Setting up Legend
light_cone = mpatches.Patch(color='black', label='1c')
blue_frame = mpatches.Patch(color='blue', label='Moving frame')

plt.legend(handles=[light_cone, blue_frame])

axvel = plt.axes([0.15, 0.1, 0.65, 0.03])
svel = Slider(axvel, 'Velocity', 0.0001, 1, valinit=.5)

def update(val):
	vel = svel.val

	time_axis0.set_ydata(t_prime_2(vel, 0))
	time_axis1.set_ydata(t_prime_2(vel, 1))
	time_axis2.set_ydata(t_prime_2(vel, 2))
	time_axis3.set_ydata(t_prime_2(vel, 3))
	time_axis4.set_ydata(t_prime_2(vel, 4))

	x_axis0.set_ydata(x_prime(vel, 0))
	x_axis1.set_ydata(x_prime(vel, 1))
	x_axis2.set_ydata(x_prime(vel, 2))
	x_axis3.set_ydata(x_prime(vel, 3))
	x_axis4.set_ydata(x_prime(vel, 4))

	fig.canvas.draw_idle()

svel.on_changed(update)

plt.show()