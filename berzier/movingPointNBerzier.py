from nBerzier import NBerzier
import numpy as np

class MovingPointNBerzier(NBerzier):
    def __init__(self, min, max, nCurves, points=None, randomNPoints = None):
        NBerzier.__init__(self, min, max,nCurves, points=points, randomNPoints = randomNPoints)
        self.currentTheta = np.array([0])
        self.currentCurve = 0
        self.currentPoint = None
    
    def movePoint(self):
        if self.currentTheta[0] >= 1:
            self.currentTheta = np.array([0])
            if self.currentCurve == -1*len(self.curves):
                self.currentCurve = 0
            else:
                self.currentCurve -= 1
        
        self.currentPoint = self.berzier(curve=self.curves[self.currentCurve], thetaInput=self.currentTheta).T[0]
        self.currentTheta = np.array([self.currentTheta[0] + 0.01])
    
    def getCurrentPoint(self):
        return self.currentPoint