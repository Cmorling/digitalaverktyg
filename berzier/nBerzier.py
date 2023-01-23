import numpy as np
import random as rnd
import math

class Nberzier():
    def __init__(self, min, max, points=None, randomNPoints = None,):
        self.points = points
        if randomNPoints and not points:
            self.points = np.array([[rnd.uniform((2/3)*min, (2/3)*max), rnd.uniform((2/3)*min, (2/3)*max)] for i in range(0,randomNPoints)]).astype(float)
        
        self.degree = len(self.points)
        self.theta = np.linspace(min, max, 10000)
        self.labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def nBerzier(self):
        scalars = []
        for i in range(0, self.degree):
            n = self.degree - 1
            k = i
            scalars.append(math.comb(n, k)*(self.theta**(n-k))*((1-self.theta)**k))

        return np.dot(self.points.T, scalars)

    def getPoints(self):
        return [{'point': p, 'label': self.labels[idx]} for idx, p in enumerate(self.points)]

        