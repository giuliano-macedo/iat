import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
import numpy as np
import matplotlib.pyplot as  plt
import argparse
from ia import LinearRegression
from ia.utils import common_argparse_alphas
from ast import literal_eval

GRAPH_TITLE,args=common_argparse_alphas()

x_linha=np.genfromtxt("../samples/entradas_x.txt")
y_linha=np.genfromtxt("../samples/saidas_y.txt")

plt.rc('text', usetex=True)
xs=np.array(range(1,args.no_it+1))
for alpha in args.interval:
	model=LinearRegression(x_linha,y_linha,alpha=alpha,normalize=args.normalize)
	errs=np.zeros((args.no_it))
	for i in range(args.no_it):
		thetao,j=next(model)
		errs[i]=j
	plt.plot(xs,errs,label=rf"$\alpha={alpha}$ $\theta={list(thetao)}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(GRAPH_TITLE)
plt.show()