import numpy as np
class Ball:
    def __init__(self, xy):
        self.currentS = xy
        self.oldS = np.array([])
        self.v = np.array([])
        self.a = 0
    
    def getCurrentPosition(self):
        return self.currentS

    def getOldPosition(self):
        return self.oldS

    def getVelocity(self):
        return self.v

    def getAcceleration(self):
        return self.a
    def setCurrentPostion(self, s):
        self.currentS = s
    
    def setOldPosition(self, s):
        self.oldS = s
    
    def setVelocity(self, v):
        self.v = v
    
    def setAcceleration(self, a):
        self.a = a