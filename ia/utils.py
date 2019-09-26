import numpy as np
def normalize_vec(X):
	assert len(X.shape)==1
	n=len(X)
	mu=np.mean(X)
	std_dev=np.sqrt(sum(((x-mu)**2 for x in X))/n)
	for i in range(n):
		X[i]=(X[i]-mu)/std_dev
