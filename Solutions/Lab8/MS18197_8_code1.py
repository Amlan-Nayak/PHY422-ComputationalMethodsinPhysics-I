import numpy as np
from sympy import *
x = symbols('x')
X = list(np.round(np.linspace(0.1,0.50, num=9),decimals=5))
F = [np.sin(i) for i in X]

Y = F
print("Forward Difference table:")
print("x=",X)
print("F(x)=",F)
for k in range(len(X)-1):  
  Y = [np.round(Y[i+1]-Y[i],decimals=5) for i in range(len(Y)-1)]
  print("Difference number "+str(k+1)+" :", Y)
  
Y = F
print("\nBackward Difference table:")
print("x=",X)
print("F(x)=",F)
for k in range(len(X)-1):  
  Y = [np.round((Y[i+1]-Y[i]),decimals=5) for i in range(len(Y)-1)]
  print("Difference number "+str(k+1)+" :", Y)

Y = F
print("\nDivided Difference table:")
print("x=",X)
print("F(x)=",F)
for k in range(len(X)-1):  
  Y = [np.round((Y[i+1]-Y[i])/(X[i+k+1]-X[i]),decimals=5) for i in range(len(Y)-1)]
  print("Difference number "+str(k+1)+" :", Y)