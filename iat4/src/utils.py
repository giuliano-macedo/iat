from PIL import Image
from ia.tpi import sobel,gaussian_blur
import numpy as np
def open_img_grey(path):
	return np.array(Image.open(path)).mean(axis=2)
def sobel_l(pic,sigma,k,l):
	return sobel(gaussian_blur(pic,sigma,k))>=l