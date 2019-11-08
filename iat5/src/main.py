import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__,*[".."]*3)))

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from ia import NN1

x=np.array([
	[0,0,1,1],
	[0,1,0,1]
])

y=np.array([[0,1,1,0]])

model=NN1(
	x,
	y,
	3,
	5,
	0.1
)

js=[]
accrs=[]

for _ in tqdm(range(1000)):
	j,accr,_=next(model)
	js.append(j)
	accrs.append(accr*100)

plt.plot(js)
plt.xlabel("Épocas")
plt.ylabel("$J$")

plt.figure()

plt.plot(accrs)
plt.xlabel("Épocas")
plt.ylabel("acúracia (%)")
plt.show()