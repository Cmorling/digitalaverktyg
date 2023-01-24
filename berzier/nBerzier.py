import numpy as np
import random as rnd
import math
from berzier import Berzier

class NBerzier(Berzier):
    def __init__(self, min, max, nCurves, points=None, randomNPoints = None):
        Berzier.__init__(self, min, max, points=points, randomNPoints = randomNPoints)
        self.nCruves = nCurves
        self.curves = [self.points]
        
        for i in range(0,self.nCruves-1):
            rPoints = self._getRandomPoints()
            rPoints[0] = self.curves[i][-1]
            if i + 2 == nCurves:
                rPoints[-1] = self.curves[0][0]
            self.curves.append(rPoints)

        #print(self.curves)
    def nBerzier(self):
        ret = None
        scalars = []
        for i in range(0, self.degree):
            n = self.degree - 1
            k = i
            scalars.append(math.comb(n, k)*(self.theta**(n-k))*((1-self.theta)**k))
        for idx, curve in enumerate(self.curves):
            if idx == 0:
                ret = np.dot(curve.T, scalars)
                continue
            ret = np.concatenate((ret, np.dot(curve.T, scalars)))
        return ret
    
    def getPoints(self):
        ret = None
        for idx, curve in enumerate(self.curves):
            if idx == 0:
                ret = curve
                continue
            ret = np.concatenate((ret, curve))
        
        return ret
    def update(self):
        newCurve = []
        for idx, curve in enumerate(self.curves):
            newPoints = []
            for point in curve:
                direction = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]).astype(float)
                direction = direction / np.linalg.norm(direction)
                newPoints.append(point + 0.25*direction)
            
            if idx != 0:
                newPoints[0] = newCurve[idx-1][-1]
            
            if np.all(curve == self.curves[-1]):
                newPoints[-1] = newCurve[0][0]
            
            newCurve.append(np.array(newPoints))
        
        self.curves = newCurve
    
    def restart(self):
        print(self.points)
        self.__init__(self.min, self.max, self.nCruves, points=None, randomNPoints=self.randomNPoints)