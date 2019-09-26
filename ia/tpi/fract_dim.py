import numpy as np
#adapted from https://gist.github.com/viveksck/1110dfca01e4ec2c608515f0d5a5b1d1
def fract_dim(Z):
	def boxcount(Z, k):
		S = np.add.reduceat(
			np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
							   np.arange(0, Z.shape[1], k), axis=1)
		return len(np.where((S > 0) & (S < k*k))[0])
	p = min(Z.shape)
	n = 2**np.floor(np.log(p)/np.log(2))
	n = int(np.log(n)/np.log(2))
	sizes = 2**np.arange(n, 1, -1)
	counts = []
	for size in sizes:
		counts.append(boxcount(Z, size))
	coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
	return -coeffs[0]