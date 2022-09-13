import numpy as np

print("f1(x) = exp(x)*x^3")
print("f2(x) = 1/sqrt(x^2 - 4)")
def f1(x):
  return np.power(x,3)*np.exp(x)
def f2(x):
  return 1/np.sqrt(np.power(x,2) - 4)

print("\nUsing Trapezoidal rule:")

X = np.linspace(-2,2,num=12)
h = X[1] - X[0]
values = [0.5*h*(f1(X[i])+ f1(X[i+1])) for i in range(len(X)-1)]
print(" Integral of f1 from (-2,2):", np.round(np.sum(values),decimals=5))
X = np.linspace(3,5,num=24)
h = X[1] - X[0]
values = [0.5*h*(f2(X[i])+ f2(X[i+1])) for i in range(len(X)-1)]
print(" Integral of f2 from (3,5):",np.round(np.sum(values),decimals=5))

print("\nUsing Simpson 1/3 rule:")
X = np.linspace(-2,2,num=12)
h = (X[1]-X[0])/2
Y = [f1(i) for i in X]
Y_half= [f1((X[i]+X[i+1])/2) for i in range(len(X)-1)]
value = (h /3) * (Y[0]+Y[-1] + 2*np.sum(Y[1:-1]) + 4*np.sum(Y_half) )
print(" Integral of f1 from (-2,2):", np.round(value,decimals=5))
X = np.linspace(3,5,num=24)
h = (X[1] - X[0])/2
Y = [f2(i) for i in X]
Y_half= [f2((X[i]+X[i+1])/2) for i in range(len(X)-1)]
value = (h /3) * (Y[0]+Y[-1] + 2*np.sum(Y[1:-1]) + 4*np.sum(Y_half) )
print(" Integral of f2 from (3,5):", np.round(value,decimals=5))

print("\nUsing Simpson 3/8 rule:")
X = np.linspace(-2,2,num=12)
h = X[1] - X[0]
Y = [f1(i) for i in X]
value = (3*h/8)*(Y[0]+Y[-1]  + 2*np.sum(Y[3:-1:3]))
for i in range(3,len(Y),3):
  Y[i] = 0
value = value +(3*h/8)*3*np.sum(Y[1:-1])
print(" Integral of f1 from (-2,2):", np.round(value,decimals=5))
X = np.linspace(3,5,num=24)
h = X[1] - X[0]
Y = [f2(i) for i in X]
value = (3*h/8)*(Y[0]+Y[-1]  + 2*np.sum(Y[3:-1:3]))
for i in range(3,len(Y),3):
  Y[i] = 0
value = value +(3*h/8)*3*np.sum(Y[1:-1])
print(" Integral of f2 from (3,5):", np.round(value,decimals=5))

print("\nUsing Boole rule:")
X = np.linspace(-2,2,num=12)
h = 2*(X[1] - X[0])
Y = [f1(i) for i in X]
value = (2*h/45)*(7*(Y[0]+Y[-1])  + 32*np.sum(Y[1:-1:2]) + 12*np.sum(Y[2:-2:4]) + 14*np.sum(Y[4:-4:4]))
print(" Integral of f1 from (-2,2):", np.round(value,decimals=5))
X = np.linspace(3,5,num=24)
h = (X[1] - X[0])
Y = [f2(i) for i in X]
value = (2*h/45)*(7*(Y[0]+Y[-1])  + 32*np.sum(Y[1:-1:2]) + 12*np.sum(Y[2:-1:4]) + 14*np.sum(Y[4:-3:4]))
print(" Integral of f2 from (3,5):", np.round(value,decimals=5))

print("\nUsing Weddle rule:")
X = np.linspace(-2,2,num=13)
h = X[1] - X[0]
Y = [f1(i) for i in X]
value = (3*h/10)*((Y[0]+Y[-1])  + 5*np.sum(Y[1:-5:6]) + np.sum(Y[2:-4:6]) + 6*np.sum(Y[3:-3:6])
+np.sum(Y[4:-2:6]) + 5*np.sum(Y[5:-1:6]))
print(" Integral of f1 from (-2,2):", np.round(value,decimals=5))
X = np.linspace(3,5,num=25)
h = X[1] - X[0]
Y = [f2(i) for i in X]
value = (3*h/10)*((Y[0]+Y[-1])  + 5*np.sum(Y[1:-5:6]) + np.sum(Y[2:-4:6]) + 6*np.sum(Y[3:-3:6])
+np.sum(Y[4:-2:6]) + 5*np.sum(Y[5:-1:6]))
print(" Integral of f2 from (3,5):", np.round(value,decimals=5))