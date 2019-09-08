import numpy as np
import matplotlib.pyplot as  plt
import argparse
from LinearRegression import LinearRegression

parser=argparse.ArgumentParser()
parser.add_argument("--no_it","-n",type=int,required=True)
parser.add_argument("--interval","-i",type=str,required=True)
parser.add_argument("--normalize",action="store_true")
args=parser.parse_args()

a,b,c=[float(o) for o in args.interval.split(",")]

x_linha=np.genfromtxt("../samples/entradas_x.txt")
y_linha=np.genfromtxt("../samples/saidas_y.txt")

plt.rc('text', usetex=True)
xs=np.array(range(1,args.no_it+1))
for alpha in np.arange(a,b+c,c):
	model=LinearRegression(x_linha,y_linha,alpha=alpha,normalize=args.normalize)
	errs=np.zeros((args.no_it))
	for i in range(args.no_it):
		thetao,j=next(model)
		errs[i]=j
	plt.plot(xs,errs,label=rf"$\alpha={alpha}$ $\theta={list(thetao)}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(rf'Gráfico de $J(\theta)$ para diferentes alphas que variam ${a}$ e ${b}$, passo {c}')
plt.show()