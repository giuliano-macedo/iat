import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))
from ia import LogisticRegression
from ia.utils import download_and_extract_zip
import matplotlib.pyplot as plt
import numpy as np
from utils import Image,listdir_imgs
from args import get_args
from tqdm import tqdm
from collections import namedtuple

def get_dataset_type(dataset_type):
	ans=[]
	for y in range(2):
		y_label=["noncat","cat"][y]
		imgs=[_Image(fname) for fname in listdir_imgs(os.path.join(args.dataset,dataset_type,y_label))]
		for img in tqdm(imgs,unit=" image",total=len(imgs),disable=False):
			x=args.method(img)
			x.append(y)
			ans.append(x)
	return np.asarray(ans,dtype=np.float).T


args=get_args()
_Image=lambda fname:Image(fname,args.sigma,args.kernel_size,args.threshold)

if (args.dataset==os.path.join("..","dataset")) and( not os.path.isdir(args.dataset)):
	url="https://llpinokio-ia.herokuapp.com/cats.zip"
	print("downloading dataset...")
	download_and_extract_zip(url,args.dataset)
print("preprocesing training")
X_train=get_dataset_type("train")
#---------------------------------------------------------------------------------
#TODO MODULARIZE
GRAPH_TITLE=""
if args.interval.type=="range":
	a,b,c=args.interval.ans;
	GRAPH_TITLE=rf'Gráfico de $J(\theta)$ para diferentes alphas que variam ${a:g}$ e ${b:g}$, passo {c:g}'
elif args.interval.type=="list":
	GRAPH_TITLE=rf'Gráfico de $J(\theta)$ para os alphas {args.interval.ans}'

ModelEntry=namedtuple("ModelEntry",["model","errs","accrs","j"])

entries=[]
for alpha in args.interval:
	model=LogisticRegression(*X_train,alpha=alpha,normalize=True)
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