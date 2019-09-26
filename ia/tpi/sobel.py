from . import conv2d
import numpy as np
def sobel(a):
	sx=np.array([
		[-1,0,+1],
		[-2,0,+2],
		[-1,0,+1]
		]
	)
	sy=np.rot90(sx,3)
	gx=conv2d(a,sx)
	gy=conv2d(a,sy)
	return np.sqrt(np.power(gx,2)+np.power(gy,2))
