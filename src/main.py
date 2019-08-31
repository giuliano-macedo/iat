import numpy as np
import matplotlib.pyplot as  plt

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
		# print(thetao.reshape(2),j)
		thetao=thetao-((alpha/m)*(X.T.dot(e)))
	return errs,thetao.reshape((2))

x_linha=np.genfromtxt("../samples/entradas_x.txt")
y_linha=np.genfromtxt("../samples/saidas_y.txt")

m=len(x_linha)
plt.rc('text', usetex=True)
NO_IT=1000
xs=np.array(range(1,NO_IT+1))
for i in np.arange(2,5.1,.5):
	prec=10**(-i)
	errs,thetao=reg_linear(x_linha,y_linha,prec,NO_IT)
	plt.plot(xs,errs,label=rf"$\alpha$=$10^{{{-i}}}$ $\theta={list(thetao)}$")
plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(r'Gráfico de $J(\theta)$ para diferente alphas')
plt.show()
# print(errs)