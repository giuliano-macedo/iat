import numpy as np
def sigmoid(z,deriv=False):
	if deriv:
		sig_z=sigmoid(z) 
		return sig_z*(1-sig_z) #https://beckernick.github.io/sigmoid-derivative-neural-network/
	return 1/(1+np.exp(-z))
def normalize_vec(X):
	assert len(X.shape)==1
	n=len(X)
	mu=np.mean(X)
	std_dev=np.sqrt(sum(((x-mu)**2 for x in X))/n)
	for i in range(n):
		X[i]=(X[i]-mu)/std_dev
