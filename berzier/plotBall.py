
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from physics import Physics
from berzier import Berzier
from ball import Ball

randomNPoints = 10

b = Berzier(-15,15, points=np.array([[-7,10],[-4,-14],[2,-9],[4,10]]))
ballPos = [3,14]
p = Physics(Ball(ballPos), b)
def onKeyRelease(event):
    print('you pressed', bytes(event.key, encoding='utf-8'), event.xdata, event.ydata)
    if event.key == ' ':
        #b.restart(-15,15, randomNPoints=randomNPoints)
        p.restart(Ball([event.xdata, event.ydata]), b)


def timerTick_Event(i):
    p.update()
    
    pointBerzier = b.berzier()
    ballPos = p.getBall().getCurrentPosition()
    collissionDetect = p.checkCollission()
    
    f = plt.gcf()
    ax = f.gca()    
    if np.all(collissionDetect):
        p.updateBallVelocity(collissionDetect)
        #ax.quiver(*ballPos, *collissionDetect, color="r", angles='xy', scale_units='xy', scale=1)
        #time.sleep(4)
    for item in ax.get_lines():
        item.remove()
    
    # for child in ax.get_children():
    #     if isinstance(child, matplotlib.text.Annotation):
    #         child.remove()
      
    # for point in nb.getPoints():
    #     ax.plot(*point, 'ro')
        #ax.annotate(point['label'], point['point']+.35, fontsize="small")
    ax.plot(*ballPos, 'ro')
    ax.plot(*pointBerzier, color=f"C0")
    
f1 = plt.figure(1)
ax = f1.add_subplot()
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)


cid = f1.canvas.mpl_connect('key_release_event', onKeyRelease)

timerTickInterval = 10
ani = FuncAnimation(f1, timerTick_Event, interval=timerTickInterval)
plt.show()

