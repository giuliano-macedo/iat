import numpy as np
from .utils import sigmoid
class NN1:
	np.random.seed(42)
	def __init__(self,x,y,number_hidden,alpha,sf=0.1):
		self.alpha=alpha

		self.x=x
		self.y=y

		self.number_hidden=number_hidden

		inputs,self.m=x.shape
		n,y_m=y.shape

		self.w1=np.random.rand(number_hidden,inputs)*sf
		self.b1=np.random.rand(number_hidden,1)*sf

		self.w2=np.random.rand(n,number_hidden)*sf
		self.b2=np.random.rand(n,1)*sf
	def forward(self,x):
		z1=(self.w1.dot(x))+self.b1
		a1=sigmoid(z1)

		z2=(self.w2.dot(a1))+self.b2
		a2=sigmoid(z2)

		return z1,a1,z2,a2

	def predict(self,x):
		return self.forward(x)[-1]

	def __iter__(self):
		return self
	def __next__(self):
		"""
		Returns:
			tuple (err,accuracy,predicted)
		"""
		z1,a1,z2,a2=self.forward(self.x)

		dz2=a2-self.y
		dw2=(1/self.m)*(dz2.dot(a1.T))
		db2=(1/self.m)*np.sum(dz2,axis=1,keepdims=True)

		dz1=(self.w2.T.dot(dz2))*(a1*(1-a1))
		dw1=(1/self.m)*(dz1.dot(self.x.T))
		db1=(1/self.m)*np.sum(dz1,axis=1,keepdims=True)


		self.w2-= self.alpha*dw2
		self.b2-= self.alpha*db2
		
		self.w1-= self.alpha*dw1
		self.b1-= self.alpha*db1

		j=1/self.m * np.sum(-self.y*np.log(a2) - (1-self.y)*np.log(1-a2))
		accr=np.sum(self.y==(a2>=0.5))/self.m

		return j,accr,a2