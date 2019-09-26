import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
import numpy as np
import matplotlib.pyplot as  plt
import argparse
from ia import LogisticRegression
from ia.utils import common_argparse_alphas
from collections import namedtuple

ModelEntry=namedtuple("ModelEntry",["model","errs","accrs","j"])

GRAPH_TITLE,args=common_argparse_alphas(need_normalize=False)

entradas=np.genfromtxt('../samples/entradas_x.txt', delimiter=',').T
saidas=np.genfromtxt('../samples/saidas_y.txt', delimiter=',')

plt.rc('text', usetex=True)
entries=[]
for alpha in args.interval:
	model=LogisticRegression(*entradas,saidas,alpha=alpha,normalize=True)
	errs=np.zeros((args.no_it))
	acrs=errs.copy()
	for i in range(args.no_it):
		acrs[i]=model.accuracy()
		thetao,j=next(model)
		errs[i]=j
	entries.append(ModelEntry(model,errs,acrs,j))
header=";".join(["alpha","j",*(f"t{i}" for i in range(len(entries[0].model.theta)))])
np.savetxt("results.csv", [
	(entry.model.alpha,entry.j,*entry.model.theta)
	for entry in entries
], delimiter=";",header=header)

xs=np.array(range(1,args.no_it+1))
for entry in entries:
	plt.plot(xs,entry.errs,label=rf"$\alpha={entry.model.alpha}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(GRAPH_TITLE)

plt.figure()
for entry in entries:
	plt.plot(xs,entry.accrs,label=rf"$\alpha={entry.model.alpha}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'acurácia')
plt.title(GRAPH_TITLE.replace(r"$J(\theta)$","acurácia"))
plt.show()