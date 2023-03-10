import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random as rnd
from matplotlib.animation import FuncAnimation
from berzier import Berzier

randomNPoints = 10

nb = Berzier(-15,15, randomNPoints=randomNPoints)

def onKeyRelease(event):
    if event.key == ' ':
        nb.restart(-15,15, randomNPoints=randomNPoints)

def timerTick_Event(i):
    
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
    
    ax.plot(*pointBerzier, label='Berzier Kurva', color="C0")

f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)

cid = f1.canvas.mpl_connect('key_release_event', onKeyRelease)

timerTickInterval = 10
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

