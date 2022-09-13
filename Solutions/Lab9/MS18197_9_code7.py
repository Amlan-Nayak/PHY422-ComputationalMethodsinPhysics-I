import numpy as np
import time
f = lambda x,y: 1/np.sqrt(x + np.power(y+1,2))
print("For f(x,y)= 1/sqrt( x + (y+1)^2 ) in x,y=(1,4)\n")
for N in [10**i for i in range(0,8)]:
  t1=time.time()
  Y= np.zeros((N,3))
  Y[:,0] = np.random.uniform(low=1, high=4, size=N)
  Y[:,1] = np.random.uniform(low=1, high=4, size=N)
  Y[:,2] = f(Y[:,0],Y[:,1])
  nt = np.mean(Y[:,2]*9)
  t2=time.time()
  print("\nMC Integration Value with N="+str(N)+":",np.round(nt,decimals=8))
  print("Time taken in secs:",np.round(t2-t1,decimals=8))