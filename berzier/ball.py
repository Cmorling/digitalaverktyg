import numpy as np
class Ball:
    def __init__(self, xy):
        self.currentS = xy
        self.oldS = np.array([])
        self.v = np.array([])
        self.a = 0
    def getPosition(self):
        return self.currentS
    def getVelocity(self):
        return self.v
    def getAcceleration(self):
        return self.a