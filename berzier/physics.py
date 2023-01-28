import numpy as np
import time
class Physics:
    def __init__(self, ball, berzier):
        self.ball = ball
        self.berzier = berzier
        self.ball.v = np.array([0,-0.01])
        self.ball.g = np.array([0,-0.06])

    def intersect(self,A,B,K,L,norm,):
        c1 = np.dot(K-A, norm)
        c2 = np.dot(L-A, norm)
        m = np.dot(np.linalg.norm(c1)/(np.linalg.norm(c1)+np.linalg.norm(c2)), L-K)+K
        direction = (A-B)[0]*(A-B)[1]
        if B[0] < A[0]:
            if m[0] > B[0] and m[0] < A[0]:
                return True
        if B[0] > A[0]:
            if m[0] < B[0] and m[0] > A[0]:
                return True
        
        return False
    
    def update(self):
        self.ball.oldS = self.ball.currentS
        self.ball.v = self.ball.v + self.ball.g
        self.ball.currentS = self.ball.currentS + self.ball.v
        
            
    def checkCollission(self):
        
        allPoints = self.berzier.berzier().T
        
        for idx, point in enumerate(allPoints):
            if idx == len(allPoints) - 1:
                continue
            berzierSegment = point - allPoints[idx + 1]
            self.berzierSegment = berzierSegment
            berzierNormal = (np.array([[0,-1], [1,0]])@berzierSegment) / np.linalg.norm(berzierSegment)
            c = np.dot(berzierNormal, (self.ball.oldS - point)) * np.dot(berzierNormal, (self.ball.currentS-point))
            if c < 0 and self.intersect(point, allPoints[idx + 1],self.ball.oldS, self.ball.currentS, berzierNormal,):
                
                return berzierNormal
        return False
    
    def updateBallVelocity(self, norm):
        vOut = np.array(self.ball.v - 2*(np.dot(self.ball.v, norm)*norm))
        self.ball.currentS=self.ball.oldS
        self.ball.v = vOut*0.95
    def restart(self, ball, berzier):
        self.__init__(ball, berzier)
    def getBall(self):
        return self.ball