import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random as rnd
from matplotlib.animation import FuncAnimation

def berzier2(t, points):
    scalars = np.array([(1-t)**3, 3*(1-t)*(1-t)*t, 3*(1-t)*t*t, t**3])
    return np.dot(points.T, scalars)

def timerTick_Event(i):
    global berzierSaved
    points = np.array([[rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)] for i in range(0,4)]).astype(float)

    f = plt.gcf()
    ax = f.gca()    
    #INSERT DELETE FUNCTION HERE
    print(ax.get_lines())
    
    for item in ax.get_lines():
        item.remove()
    for child in ax.get_children():
        if isinstance(child, matplotlib.text.Annotation):
            child.remove()
    for idx,point in enumerate(points):
        ax.plot(*point, 'ro')
        ax.annotate(['A', 'B', 'C', 'D'][idx], point+.35, fontsize="small")

    theta = np.linspace(-10, 10, 1000)
    pointBerzier = berzier2(theta, points)
    ax.plot(*pointBerzier, label='Berzier Kurva')

f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)
#ax.legend()

timerTickInterval = 2000
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

