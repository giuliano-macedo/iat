import PIL
from ia.tpi import sobel,gaussian_blur,humoments,fract_dim
from argparse import ArgumentTypeError
import numpy as np
import os
import re
from pathlib import Path
def listdir_imgs(path):
	number_re=re.compile(r"\d+")
	get_last_no=lambda s:int(list(number_re.finditer(s))[-1].group(0))
	dirs=sorted(os.listdir(path),key=get_last_no)
	for ans in dirs:
		if os.path.splitext(ans)[1] not in {".png",".gif",".jpeg",".jpg"}:
			continue
		yield os.path.join(path,ans)
class Image(object):
	def __init__(self, fname,sigma,k,l):
		self.name=Path(fname).stem
		self.original=np.array(PIL.Image.open(fname)).mean(axis=2)
		self.processed=np.empty(0)
		self.sigma=sigma
		self.k=k
		self.l=l
	def get_processed_img(self):
		if not self.processed.any():
			self.processed=sobel(gaussian_blur(self.original,self.sigma,self.k))>=self.l
		return self.processed
	def __repr__(self):
		return "<Image %s>"%self.name
class FeatureExtractor:
	methods={
		"humoments":lambda img:humoments(img.get_processed_img()),
		"fractdim":lambda img:[fract_dim(img.get_processed_img())],
		"histogram":lambda img:np.histogram(img.original,range(0,256))[0],
		"pixels":lambda img:img.original.reshape(-1)
	}
	methods_name={
		"humoments":"momentos de hu",
		"fractdim":"dimensão fractal",
		"histogram":"histograma",
		"pixels":"pixels"
	}
	def __init__(self,s):
		s=s.split(",")
		if not all(m in self.methods.keys() for m in s):
			raise ArgumentTypeError("invalid method")
		self.str=",".join([self.methods_name[m] for m in s])
		self.pipeline=[self.methods[k] for k in s]
	def __str__(self):
		return self.str
	def __call__(self,img):#this is probably slow
		ans=[]
		for f in self.pipeline:
			ans.extend(f(img))
		return ans
