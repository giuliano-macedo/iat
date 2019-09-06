import numpy as np
import matplotlib.pyplot as  plt
import argparse

def reg_linear(x_linha,y_linha,alpha,no_it):
	m=len(x_linha)
	Y=y_linha.reshape(m,1)
	X=np.ones((m,2))
	X[:,1]=x_linha
	# t1*x+t0
	thetao=np.array([
		[0],
		[0]
	])
	errs=np.zeros((no_it))
	for i in range(no_it):
		H_theta=X.dot(thetao)
		e=H_theta-Y
		j=(e.T.dot(e)/(2*m)).reshape(())
		errs[i]=j
		thetao=thetao-((alpha/m)*(X.T.dot(e)))
	return errs,thetao.reshape((2))

parser=argparse.ArgumentParser()
parser.add_argument("--no_it","-n",type=int,required=True)
parser.add_argument("--interval","-i",type=str,required=True)
args=parser.parse_args()

NO_IT=args.no_it
a,b,c=[float(o) for o in args.interval.split(",")]

x_linha=np.genfromtxt("../samples/entradas_x.txt")
y_linha=np.genfromtxt("../samples/saidas_y.txt")

m=len(x_linha)
plt.rc('text', usetex=True)
xs=np.array(range(1,NO_IT+1))
for alpha in np.arange(a,b+c,c):
	errs,thetao=reg_linear(x_linha,y_linha,alpha,NO_IT)
	plt.plot(xs,errs,label=rf"$\alpha={alpha}$ $\theta={list(thetao)}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(rf'Gráfico de $J(\theta)$ para diferentes alphas que variam ${a}$ e ${b}$, passo {c}')
plt.show()