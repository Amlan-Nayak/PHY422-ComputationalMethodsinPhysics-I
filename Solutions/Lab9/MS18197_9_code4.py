import numpy as np
def f(x):
  return np.sqrt(1+np.power(np.cos(x),2))
N = [np.power(2,k) for k in range(1,11)]
I= []
for n in N:
  X= np.linspace(0,48,n)
  F = np.array([[f(i) for i in X]],dtype=float)
  h= X[1]-X[0]
  I.append((h/2)*(F[0,0]+F[0,-1] + 2*(np.sum(F[0,1:-1]))))
Y = I
for j in range(len(I)-1):
  Y = [((4**(j+1))*Y[m+1] - Y[m])/(4**(j+1) - 1) for m in range(0,len(Y)-1)]
print("Using the Romberg method")
print("Value of integral of f(x) = sqrt((cos(x))^2+1) over (0,48) is:", Y)