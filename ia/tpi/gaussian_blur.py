from . import conv2d
import numpy as np
g=lambda x,y,std_dev:(1/(2*np.pi*np.power(std_dev,2)))*np.exp(-(np.power(x,2)+np.power(y,2))/(2*np.power(std_dev,2)))
def gaussian_blur(a,std_dev=1,kernel_size=3):
	gauss=np.zeros((kernel_size,kernel_size))
	for i in range(kernel_size):
		for j in range(kernel_size):
			gauss[i][j]=g(i-(kernel_size/2),j-(kernel_size/2),std_dev)
	return conv2d(a,gauss)
