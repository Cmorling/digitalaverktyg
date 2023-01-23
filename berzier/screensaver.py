import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random as rnd
from matplotlib.animation import FuncAnimation
from nBerzier import Nberzier
oldPoints = []
oldPoints2 = []

def timerTick_Event(i):
    global oldPoints
    global oldPoints2
    
    nb = None
    
    if len(oldPoints) == 0:
        nb = Nberzier(-15, 15, randomNPoints=10) #Här väljer man antal punkter
    else:
        newPoints = []
        for point in oldPoints:
            direction = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]).astype(float)
            direction = direction / np.linalg.norm(direction)
            newPoints.append(point + 0.1*direction)
        nb = Nberzier(-15, 15, np.array(newPoints))
    
    pointBerzier = nb.nBerzier()
    oldPoints = nb.getWithoutLabels()
    
    nb2 = None
    
    if len(oldPoints2) == 0:
        nb2 = Nberzier(-15, 15, oldPoints[::-1]) #Här väljer man antal punkter
    else:
        newPoints = []
        for point in oldPoints2:
            direction = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]).astype(float)
            direction = direction / np.linalg.norm(direction)
            newPoints.append(point + 0.1*direction)
        
        newPoints[0] = oldPoints[0]
        newPoints[-1] = oldPoints[-1]
        nb2 = Nberzier(-15, 15, np.array(newPoints))
    
    pointBerzier2 = nb2.nBerzier()
    oldPoints2 = nb2.getWithoutLabels()
    
    f = plt.gcf()
    ax = f.gca()    
    
    for item in ax.get_lines():
        item.remove()
    
    for child in ax.get_children():
        if isinstance(child, matplotlib.text.Annotation):
            child.remove()
      
    # for point in nb.getPoints():
    #     ax.plot(*point['point'], 'ro')
    #     ax.annotate(point['label'], point['point']+.35, fontsize="small")
    
    ax.plot(*pointBerzier, label='Berzier Kurva', color='green')
    ax.plot(*pointBerzier2, label='Berzier Kurva', color='green')

f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)

timerTickInterval = 5
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

