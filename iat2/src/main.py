import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
import numpy as np
import matplotlib.pyplot as  plt
import argparse
from ia import LinearRegression
from ia.utils import common_argparse_alphas

GRAPH_TITLE,args=common_argparse_alphas(need_normalize=False)

data=np.genfromtxt('../samples/winequality-red.csv', delimiter=';')[1:]


plt.rc('text', usetex=True)
xs=np.array(range(1,args.no_it+1))
ans=[]
for alpha in args.interval:
	model=LinearRegression(*data.T,alpha=alpha,normalize=True)
	errs=np.zeros((args.no_it))
	for i in range(args.no_it):
		thetao,j=next(model)
		errs[i]=j
	ans.append([alpha,j,*thetao])
	plt.plot(xs,errs,label=rf"$\alpha={alpha}$")
header=";".join(["alpha","j",*(f"t{i}" for i in range(12))])
np.savetxt("results.csv", ans, delimiter=";",header=header)
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(GRAPH_TITLE)
plt.show()