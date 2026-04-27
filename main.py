import matplotlib.pyplot as mpl
from solver import *
from resources import *
import numpy as np
import matplotlib.animation as animation

# x, v, a, t = solver(0.005, 100, 0.5, 0.0, 5, 1)
x, v, a, t = solver(0.5, 100000, 0.5, 0.0, 5, 1)
fig, ax = mpl.subplots()
ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-', lw=2)

x_pos, y_pos = convert_to_positional(x, 1)

def update(frame):
  line.set_data([0, x_pos[frame]], [0, y_pos[frame]])
  return line,

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=20, blit=True)
mpl.show()