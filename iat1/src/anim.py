import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import argparse
from ia import LinearRegression

class Animation:
	def __init__(self,alpha,normalize,skip=1):
		self.skip=skip
		self.x_linha=np.genfromtxt("../samples/entradas_x.txt")
		self.y_linha=np.genfromtxt("../samples/saidas_y.txt")
		self.model=LinearRegression(self.x_linha,self.y_linha,alpha=alpha,normalize=normalize)
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
		t0,t1=self.model.theta.reshape(2)
		h=lambda xs:[t0+(t1*x) for x in xs]
		ax1.plot(
			self.axis[:2],
			h(self.axis[:2]),
			color="red",
			label=rf"$\theta={[t0,t1]}$"
		)
		for _ in range(self.skip):
			j=next(self.model)[1]

		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(rf'$\alpha={self.model.alpha:.2e},it={i*self.skip},j={j:e}$') 
		plt.legend(fontsize=8)

parser=argparse.ArgumentParser()
parser.add_argument("--alpha","-a",type=float,required=True)
parser.add_argument("--skip","-s",type=int,required=True)
parser.add_argument("--normalize",action="store_true")
args=parser.parse_args()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
anim=Animation(args.alpha,args.normalize,args.skip)
ani = animation.FuncAnimation(fig, anim.animate, interval=1) 
plt.show()