import numpy as np
from sympy import *
x = symbols('x')
X = list(np.round(np.linspace(0.1,0.50, num=9),decimals=4))
F = [np.round(np.sin(i),decimals=4) for i in X]
exp= F[0]
Y=F
for k in range(len(X)-1):  
  Y = [np.round((Y[i+1]-Y[i])/(X[i+k+1]-X[i]),decimals=4) for i in range(len(Y)-1)]
  sum=1
  for j in range(k+1):
    sum= (x-X[j])*sum
  exp = exp + sum*Y[0]
print("\nDivided Difference Interpolation Polynomial")
for i in [0.13,0.23,0.39,0.47]:
  print("\nThe value of Interpolation Polynomial at "+str(i)+":" ,exp.subs(x,i))
  print("The value of sine function at "+str(i)+":",np.sin(i))
  print("Error % between interpolation and actual value:",100*abs((exp.subs(x,i)-np.sin(i))/np.sin(i)))


exp= F[0]
Y=F
h=0.05
for k in range(len(X)-1):  
  Y = [np.round(Y[i+1]-Y[i],decimals=4) for i in range(len(Y)-1)]
  sum=1
  for j in range(k+1):
    sum= ((x-X[j])*sum) 
  exp = exp + sum*Y[0]/((factorial(j+1))*(h**(j+1)))
print("\nForward Difference Polynomial")
print("\nThe value of Interpolation Polynomial at 0.13: ",exp.subs(x,0.13))
print("The value of sine function at 0.13: ",np.sin(0.13))
print("Error % between interpolation and actual value:",100*abs((exp.subs(x,0.13)-np.sin(0.13))/np.sin(0.13)))

X=X[::-1]
F=F[::-1]
exp= F[0]
Y=F
h=0.05
for k in range(len(X)-1):  
  Y = [np.round(-Y[i+1]+Y[i],decimals=4) for i in range(len(Y)-1)]
  sum=1
  for i in range(0,k+1):
    sum= (x-X[i])*sum 
  exp = exp + (sum*Y[0])/ (factorial(i+1)*(h**(i+1)))
print("\nBackward Difference Polynomial")
print("\nThe value of Interpolation Polynomial at 0.47: ",exp.subs(x,0.47))
print("The value of sine function at 0.47: ",np.sin(0.47))
print("Error % between interpolation and actual value:",100*abs((exp.subs(x,0.47)-np.sin(0.47))/np.sin(0.47)))