import numpy as np
import time
f = lambda x: 1/(x**2-4)**(0.5)
print("For f(x)= 1/sqrt(x^2 - 4) in x=(3,5)\n")
for N in [10**i for i in range(1,8)]:
  t1=time.time()
  Y= np.zeros((N,2))
  Y[:,0] = np.random.uniform(low=3, high=5, size=N)
  Y[:,1] = f(Y[:,0])
  nt = np.mean(Y[:,1]*(2))
  t2=time.time()
  print("MC Integration Value with N="+str(N)+":",np.round(nt,decimals=8))
  print("Time taken in secs:",np.round(t2-t1,decimals=8))
f = lambda x: np.sqrt(1+np.power(np.cos(x),2))
print("\nFor f(x)= sqrt(cos(x)^2 + 1) in x=(0,48)\n")
for N in [10**i for i in range(1,8)]:
  t1=time.time()
  Y= np.zeros((N,2))
  Y[:,0] = np.random.uniform(low=0, high=48, size=N)
  Y[:,1] = f(Y[:,0])
  nt = np.mean(Y[:,1]*(48))
  t2=time.time()
  print("MC Integration Value with N="+str(N)+":",np.round(nt,decimals=8))
  print("Time taken in secs:",np.round(t2-t1,decimals=8))