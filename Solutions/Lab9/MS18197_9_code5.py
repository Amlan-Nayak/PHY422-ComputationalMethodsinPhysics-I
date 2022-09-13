import numpy as np

def f(x):
  return 1/(1+x)
N = [np.power(2,k) for k in range(1,10)]
I= []
for n in N:
  X= np.linspace(0,1,n)
  F = np.array([[f(i) for i in X]],dtype=float)
  h= X[1]-X[0]
  I.append((h/2)*(F[0,0]+F[0,-1] + 2*(np.sum(F[0,1:-1]))))
Y = I
for j in range(len(I)-1):
  Y = [((4**(j+1))*Y[m+1] - Y[m])/(4**(j+1) - 1) for m in range(0,len(Y)-1)]
print("Value of integral of f(x) = 1/(1+x) over (0,1) is:", Y)


def g(t):
  return 1/(3+t)
print("\nChanging variables in f(x) gives us g(t)= 1/(3+t) over (-1,1)")
print("f(x) and g(t)= 1/(3+t) are equivalent")
print("\nValue of integral through gauss one point method:", 2*(g(0)))
m= 1/np.sqrt(3)
print("Value of integral through gauss two point method:", g(m)+  g(-m) )
m= np.sqrt(3/5)
val = (1/9)*(5*g(-m)+ 8*g(0)+5*g(m))
print("Value of integral through gauss three point method:", val ) 