import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

quivers_artist = []

def timerTick_Event(i):
    global quivers_artist
    
    v1 = np.array([rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)]).astype(float)
    #v1 = v1 / np.linalg.norm(v1)
    
    v2 = np.array([rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)]).astype(float)
    #v2 = v2 / np.linalg.norm(v2)
    
    mat = np.column_stack((v1, v2))
    print(mat)
    f = plt.gcf()
    ax = f.gca()    
    #INSERT DELETE FUNCTION HERE
    if len(quivers_artist) > 0:
        for q in quivers_artist:
            q.remove()
        quivers_artist.clear()
    quivers_artist.append(ax.quiver(0, 0, mat[0,0], mat[0,1], color="r", angles='xy', scale_units='xy', scale=1))
    quivers_artist.append(ax.quiver(0, 0, mat[1,0], mat[1,1], color="g", angles='xy', scale_units='xy', scale=1))


f1 = plt.figure(1)
ax = f1.add_subplot()

u = ax.quiver(0, 0, 0, 0, color="r")
v = ax.quiver(0, 0, 0, 0, color="g")
# set empty line plots with colors associate to the
# quivers. Doing so we can show a legend.
ax.plot([], [], color="r", label="X")
ax.plot([], [], color="g", label="Y")

ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
ax.set_xlabel("X_AXIS"); ax.set_ylabel("Y_AXIS")
ax.legend()

timerTickInterval = 1000
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()