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
	ans=np.asarray(ans,dtype=np.float)
	np.random.shuffle(ans)
	return ans.T


args=get_args()
_Image=lambda fname:Image(fname,args.sigma,args.kernel_size,args.threshold)

if (args.dataset==os.path.join("..","dataset")) and( not os.path.isdir(args.dataset)):
	url="https://llpinokio-ia.herokuapp.com/cats.zip"
	print("downloading dataset...")
	download_and_extract_zip(url,args.dataset)
print("preprocesing training")
X_train=get_dataset_type("train")
print("preprocesing evaluation")
X_eval =get_dataset_type("evaluation")

model_train=LogisticRegression(*X_train,alpha=args.alpha,normalize=args.normalize)
model_eval=LogisticRegression(*X_eval,alpha=args.alpha,normalize=args.normalize) #TODO: preety hacky
#---------------------------------------------------------------------------------
#TODO MODULARIZE
GRAPH_TITLE=rf"""Gráfico de $J(\theta)$ do dataset de treino e validação para $\alpha={args.alpha}$ 
 utilizando o(s) métodos(s) de {str(args.method)}
 {["sem","com"][args.normalize]} normalização de entrada"""


j_train=np.zeros((args.no_it))
acrs_train=j_train.copy()

j_eval=j_train.copy()
acrs_eval=j_train.copy()


print("training alpha=",args.alpha)
for i in tqdm(range(args.no_it)):
	acrs_train[i]=model_train.accuracy()
	j_train[i]=next(model_train)[1]
	
	model_eval.theta=model_train.theta.copy()
	acrs_eval[i]=model_eval.accuracy()
	j_eval[i]=next(model_eval)[1]

header=";".join(["alpha","j",*(f"t{i}" for i in range(len(model_train.theta)))])
np.savetxt("results.csv", [
	(model_train.alpha,j_train[-1],*model_train.theta)
], delimiter=";",header=header)

xs=np.array(range(1,args.no_it+1))

plt.plot(xs,j_train,label=rf"treino")
plt.plot(xs,j_eval,label=rf"evaluação")

plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'$J(\theta)$')
plt.title(GRAPH_TITLE)

plt.figure()

plt.plot(xs,acrs_train,label=rf"treino")
plt.plot(xs,acrs_eval,label=rf"evaluação")

plt.legend(fontsize=8)
plt.xlabel('Números de iteração')
plt.ylabel(r'acurácia')
plt.title(GRAPH_TITLE.replace(r"$J(\theta)$","acurácia"))

plt.show()