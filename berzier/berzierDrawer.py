import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from berzier import Berzier


nb = Berzier(-15, 15, randomNPoints=4) #Här väljer man antal punkter
pointBerzier = nb.berzier()

f1 = plt.figure(1)
ax = f1.add_subplot()

ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)

for point in nb.getPoints():
    ax.plot(*point['point'], 'ro')
    ax.annotate(point['label'], point['point']+.35, fontsize="small")

ax.plot(*pointBerzier, label='Berzier Kurva')
ax.legend()

plt.show()

