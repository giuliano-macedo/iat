
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import argparse

class Animation:
	def __init__(self,alpha,skip=1):
		self.skip=skip
		self.alpha=alpha
		self.x_linha=np.genfromtxt("../samples/entradas_x.txt")
		self.y_linha=np.genfromtxt("../samples/saidas_y.txt")

		self.m=len(self.x_linha)
		self.Y=self.y_linha.reshape(self.m,1)
		self.X=np.ones((self.m,2))
		self.X[:,1]=self.x_linha
		self.thetao=np.array([[0],[0]])
		border=.1
		self.axis=np.array([
			min(self.x_linha)-border, 
			max(self.x_linha)+border,
			min(self.y_linha)-border, 
			max(self.y_linha)+border
		])

	def animate(self,i):
		ax1.clear()
		plt.axis(self.axis)
		ax1.scatter(self.x_linha, self.y_linha)
		t0,t1=self.thetao.reshape(2)
		h=lambda xs:[t0+(t1*x) for x in xs]
		ax1.plot(
			self.axis[:2],
			h(self.axis[:2]),
			color="red",
			label=rf"$\theta={[t0,t1]}$"
		)
		
		for _ in range(self.skip):
			H_theta=self.X.dot(self.thetao)
			e=H_theta-self.Y
			j=float(e.T.dot(e))/(2*self.m)
			self.thetao=self.thetao-((self.alpha/self.m)*(self.X.T.dot(e)))

		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(rf'$\alpha={self.alpha:.2e},it={i*self.skip},j={j:e}$') 
		plt.legend(fontsize=8)

parser=argparse.ArgumentParser()
parser.add_argument("alpha",type=float)
parser.add_argument("skip",type=int)
args=parser.parse_args()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
anim=Animation(args.alpha,args.skip)
ani = animation.FuncAnimation(fig, anim.animate, interval=1) 
plt.show()