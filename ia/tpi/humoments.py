import numpy as np
#this code is adapted from https://github.com/llpinokio/proct2
def humoments(i):
	def M(p,q):
		ans=0
		h,w=i.shape
		for y in range(h):
			for x in range(w):
				if i[x][y]:
					ans+=pow(x,p)*pow(y,q)
		return ans
	def mu(p,q):
		ans=0
		h,w=i.shape
		for y in range(h):
			for x in range(w):
				if i[x][y]:
					ans+=pow((x-xbar),p)*pow((y-ybar),q)
		return ans
	# def mu(p,q):
	# 	ans=0
	# 	h,w=i.shape
	# 	gamma=1+((p+q)/2)
	# 	return eta(p,q)/pow(eta00,gamma)
	m00=M(1,1)
	xbar=M(1,0)/m00
	ybar=M(0,1)/m00

	# eta00=eta(0,0)

	u11=mu(1,1)
	u20=mu(2,0)
	u02=mu(0,2)

	u21=mu(2,1)
	u12=mu(1,2)

	u30=mu(3,0)
	u03=mu(0,3)

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

	# print(ans)
	# breakpoint()
	return ans