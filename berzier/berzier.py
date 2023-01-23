import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def berzier(t, points):
    scalars = np.array([(1-t)**3, 3*(1-t)*(1-t)*t, 3*(1-t)*t*t, t**3])
    return np.dot(points.T, scalars)

ax = plt.figure().add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)
points = np.array([[rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)] for i in range(0,4)]).astype(float)

for idx,point in enumerate(points):
    ax.plot(*point, 'ro')
    ax.annotate(['A', 'B', 'C', 'D'][idx], point+.35, fontsize="small")

theta = np.linspace(-15, 15, 1000)
pointBerzier = berzier(theta, points)
ax.plot(*pointBerzier, label='Berzier Kurva')
ax.legend()

plt.show()

