import numpy as np
import random as rnd
import math

class Berzier():
    def __init__(self, min, max, points=None, randomNPoints = None,):
        self.min = min
        self.max = max
        self.randomNPoints = randomNPoints
        self.points = points
        
        if randomNPoints and not points:
            self.points = self._getRandomPoints()
        self.degree = len(self.points)
        self.theta = np.linspace(0, 1, 10000)
        self.labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def _getRandomPoints(self):
        return np.array([[rnd.uniform((9/10)*self.min, (9/10)*self.max), rnd.uniform((9/10)*self.min, (9/10)*self.max)] for i in range(0,self.randomNPoints)]).astype(float)
    
    def berzier(self, curve=None):
        currentCurve = self.points
        if np.all(curve):
            currentCurve = curve
        scalars = []
        for i in range(0, self.degree):
            n = self.degree - 1
            k = i
            scalars.append(math.comb(n, k)*(self.theta**(n-k))*((1-self.theta)**k))

        return np.dot(currentCurve.T, scalars)

    def getPoints(self):
        return [{'point': p, 'label': self.labels[idx]} for idx, p in enumerate(self.points)]
    def getWithoutLabels(self):
        return self.points
    def restart(self):
        self.__init__(self.min, self.max, points=None, randomNPoints=self.randomNPoints)
        