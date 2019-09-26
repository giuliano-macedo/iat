import numpy as np
from . import LinearRegression
__author__="Giuliano Oliveira"
class LogisticRegression(LinearRegression):
	def __next__(self):
		"""Step in iteration, returns curr theta and j"""
		H_theta=np.divide(1,1+np.exp(-self.X.dot(self.theta)))
		e=H_theta-self.Y
		j=1/self.m * np.sum(-self.Y*np.log(H_theta) - (1-self.Y)*np.log(1-H_theta))
		self.theta-=self.alpha*(self.X.T.dot(e))
		return self.theta.reshape(self.n+1),j
	def accuracy(self):
		H_theta=np.divide(1,1+np.exp(-self.X.dot(self.theta)))
		prediction= H_theta>=0.5
		currect=prediction==self.Y
		return np.sum(currect)/self.m