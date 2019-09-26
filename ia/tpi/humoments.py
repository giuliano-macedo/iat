import numpy as np
#this code is adapted from https://github.com/llpinokio/proct2

def regularMomentOrder(i,p,q):
	ans=0
	h,w=i.shape
	for y in range(h):
		for x in range(w):
			if i[x][y]:
				ans+=pow(x,p)*pow(y,q)
	return ans
def mu(i,a,xmean,ymean,p,q):
	ans=0
	h,w=i.shape
	for y in range(h):
		for x in range(w):
			if i[x][y]:
				ans+=pow((x-xmean),p)*pow((y-ymean),q)
	return ans

def humoments(i):
	a=regularMomentOrder(i,1,1)
	xm=regularMomentOrder(i,1,0)/a
	ym=regularMomentOrder(i,0,1)/a

	u11=mu(i,a,xm,ym,1,1)
	u20=mu(i,a,xm,ym,2,0)
	u02=mu(i,a,xm,ym,0,2)

	u21=mu(i,a,xm,ym,2,1)
	u12=mu(i,a,xm,ym,1,2)

	u30=mu(i,a,xm,ym,3,0)
	u03=mu(i,a,xm,ym,0,3)

	ans=[]

	temp1=u20+u02

	ans.append(temp1)#phi1

	ans.append((temp1*temp1)+(4*u11*u11))#phi2

	temp1=u30-(3*u12);
	temp2=(3*u21)-u03;
	ans.append((temp1*temp1)+(temp2*temp2))#phi3

	temp1=u30+u12;
	temp2=u21+u03;

	temp1*=temp1;
	temp2*=temp2;
	ans.append(temp1+temp2)#phi4

	ans.append((u30-(3*u12))*(u30+u12)*(temp1-(3*temp2))+((3*u21-u03)*(u21+u03)*((3*temp1)-temp2)))#phi5

	ans.append( ((u20-u02)*(temp1-temp2)) +(4*u11*(u30+u12)*(u21+u03)))#phi6

	ans.append( (((3*u21)-u03)*(u30+u12)*(temp1-3*temp2)) - ((u30 - (3*u12))*(u21+u03)*((3*temp1) - temp2)))#phi7

	return ans