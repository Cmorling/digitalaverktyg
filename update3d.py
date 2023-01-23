import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

quivers_artist = []

def timerTick_Event(i):
    global quivers_artist
    temp1 = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]).astype(float)
    temp1 = temp1 / np.linalg.norm(temp1)
    v2 = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]).astype(float)
    v2 = v2 / np.linalg.norm(v2)
    v3 = np.cross(temp1, v2)
    v3 = v3 / np.linalg.norm(v3)
    v1 = np.cross(v2, v3)
    v1 = v1 / np.linalg.norm(v1)    
    mat = np.column_stack((v1, v2, v3))
    f = plt.gcf()
    ax = f.gca()    
    #INSERT DELETE FUNCTION HERE
    if len(quivers_artist) > 0:
        for q in quivers_artist:
            q.remove()
        quivers_artist.clear()
    quivers_artist.append(ax.quiver(0, 0, 0, mat[0,0], mat[0,1], mat[0,2], color="r"))
    quivers_artist.append(ax.quiver(0, 0, 0, mat[1,0], mat[1,1], mat[1,2], color="g"))
    quivers_artist.append(ax.quiver(0, 0, 0, mat[2,0], mat[2,1], mat[2,2], color="b"))


f1 = plt.figure(1)
ax = f1.add_subplot(projection='3d')

u = ax.quiver(0, 0, 0, 0, 0, 0, color="r")
v = ax.quiver(0, 0, 0, 0, 0, 0, color="g")
w = ax.quiver(0, 0, 0, 0, 0, 0, color="b")
# set empty line plots with colors associate to the
# quivers. Doing so we can show a legend.
ax.plot([], [], [], color="r", label="X")
ax.plot([], [], [], color="g", label="Y")
ax.plot([], [], [], color="b", label="Z")

ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-1.1, 1.1)
ax.set_xlabel("X_AXIS"); ax.set_ylabel("Y_AXIS"); ax.set_zlabel("Z_AXIS")
ax.legend()

timerTickInterval = 1000
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()