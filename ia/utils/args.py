from ast import literal_eval
from argparse import ArgumentTypeError
from ast import literal_eval
from math import ceil
import numpy as np
class Interval:
	__is_float_tuple3=lambda o:isinstance(o,tuple) and len(o)==3 and all(isinstance(x, (float,int)) for x in o)
	__is_float_list	=lambda o:isinstance(o,list) and all(isinstance(x, (float,int)) for x in o)
	def __init__(self,s):
		self.type=""
		try:
			self.ans=literal_eval(s)
		except Exception:
			raise ArgumentTypeError("invalid interval")
		if Interval.__is_float_tuple3(self.ans):
			a,b,c=self.ans
			self.type="range"
			self.data=(float(f"{x:g}") for x in np.arange(a,b+c,c)[0:ceil((b-a)/c)+1])
		elif Interval.__is_float_list(self.ans):
			self.type="list"
			self.data=self.ans
		else:
			raise ArgumentTypeError("unrecognized interval")
	def __iter__(self):
		return iter(self.data)
def parse_interval(s):
	return Interval(s)