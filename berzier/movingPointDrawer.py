import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from movingPointNBerzier import MovingPointNBerzier
import time

nBerziers = 3
randomNPoints = 5

nb = MovingPointNBerzier(-15,15, nBerziers, randomNPoints=randomNPoints)

def onKeyRelease(event):
    print('you pressed', bytes(event.key, encoding='utf-8'), event.xdata, event.ydata)
    if event.key == ' ':
        nb.restart()

def timerTick_Event(i):
    global nb
    if i > 0:
        #nb.update()
        pass
    nb.movePoint()
    movingPoint = nb.getCurrentPoint()
    pointBerzier = nb.nBerzier()
    
    f = plt.gcf()
    ax = f.gca()    
    
    for item in ax.get_lines():
        item.remove()
    
    # for child in ax.get_children():
    #     if isinstance(child, matplotlib.text.Annotation):
    #         child.remove()
      
    # for point in nb.getPoints():
    #     print(point)
    #     ax.plot(*point, 'ro')
        #ax.annotate(point['label'], point['point']+.35, fontsize="small")
    #print(*movingPoint)
    ax.plot(*movingPoint, 'ro')
    ax.plot(*pointBerzier, color=f"C0")
    
f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)


cid = f1.canvas.mpl_connect('key_release_event', onKeyRelease)

timerTickInterval = 10
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

