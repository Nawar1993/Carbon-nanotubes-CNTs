import numpy as np
import random
gap=0.62
T=0.003
samples=10000000
result=[]
cc=14.64
dd=-25.52
gg=6.21
aa=-8.52
ba=23.3
ab=5.81
bb=11.6
ca=-0.491
cb=-0.482
for i in range(samples):
	n=random.randint(0,1000)
	m=random.randint(0,1000)
	k=np.sqrt(n**2  +m**2  +n*m)
	d=2.46/np.pi  *k
	teta=np.arccos((2*n+m)/(2*np.sqrt(n**(2) +m**(2) +n*m)))
	if (n-m)%3 ==1:
		Eg1=cc/k +dd/k**2  +(1/k**2  +gg/k**3)*(aa +ba*np.exp(ca*(n-m)))*(4*np.cos(teta) *np.cos(teta) -3*np.cos(teta))
		error1=abs(Eg1-gap)
		if error1<T:
			result.append((round(n,1),round(m,1),round(Eg1,3),round(d,2)))
			for x in result:
			     print(f"n:{x[0]},m:{x[1]},Eg(eV):{x[2]},d(A):{x[3]}")
	elif (n-m)%3 ==2:
	       Eg2=cc/k +dd/k**2 +(1/k**2 +gg/k**3)*(ab +bb*np.exp(cb*(n-m)))*(4*np.cos(teta) *np.cos(teta) -3*np.cos(teta))
	       error2=abs(Eg2-gap) 
	       if error2<T:
        	result.append((round(n,0),round(m,0),round(Eg2,3),round(d,2)))
        	for x in result:
        		print(f"n:{x[0]},m:{x[1]},Eg(eV):{x[2]},d(A):{x[3]}")    
