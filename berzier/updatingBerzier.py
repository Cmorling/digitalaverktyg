import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random as rnd
from matplotlib.animation import FuncAnimation
from berzier import Berzier

def timerTick_Event(i):
    global berzierSaved
    
    nb = Berzier(-15, 15, randomNPoints=6) #Här väljer man antal punkter
    pointBerzier = nb.berzier()

    f = plt.gcf()
    ax = f.gca()    
    
    for item in ax.get_lines():
        item.remove()
    
    for child in ax.get_children():
        if isinstance(child, matplotlib.text.Annotation):
            child.remove()
      
    for point in nb.getPoints():
        ax.plot(*point['point'], 'ro')
        ax.annotate(point['label'], point['point']+.35, fontsize="small")
    
    ax.plot(*pointBerzier, label='Berzier Kurva')

f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)

timerTickInterval = 1000
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

