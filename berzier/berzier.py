import numpy as np
import random as rnd
import math

class Berzier():
    def __init__(self, min, max, points=None, randomNPoints = None,):
        self.min = min
        self.max = max
        self.randomNPoints = randomNPoints
        self.points = points
        
        if randomNPoints and not np.all(points != None):
            print('assigning ranodm points', np.all(points), points)
            self.points = self._getRandomPoints()
        self.degree = len(self.points)
        self.theta = np.linspace(0, 1, 100)
        self.labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.saved = None
    def _getRandomPoints(self):
        return np.array([[rnd.uniform((9/10)*self.min, (9/10)*self.max), rnd.uniform((9/10)*self.min, (9/10)*self.max)] for i in range(0,self.randomNPoints)]).astype(float)
    
    def berzier(self, curve=None, thetaInput=None):
        if not np.all(curve) and np.all(self.saved != None):
            return self.saved
        currentCurve = self.points
        theta = self.theta
        
        if np.all(curve):
            currentCurve = curve

        if np.all(thetaInput) != None:
            theta = thetaInput
        
        scalars = []
        for i in range(0, self.degree):
            n = self.degree - 1
            k = i
            scalars.append(math.comb(n, k)*(theta**(n-k))*((1-theta)**k))
        ret = np.dot(currentCurve.T, scalars)
        if not np.all(currentCurve):
            self.saved = ret
        return ret

    def getPoints(self):
        return [{'point': p, 'label': self.labels[idx]} for idx, p in enumerate(self.points)]
    def getWithoutLabels(self):
        return self.points
    def restart(self, min, max, points=None, randomNPoints = None):
        self.__init__(min, max, points=points, randomNPoints=randomNPoints)
        