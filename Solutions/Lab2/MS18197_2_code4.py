import numpy as np
print("Find root of equation for f(x)=x**3 - x - exp(x) - 2 in the interval [2,3]")
def f(x):
 return x**3 - x - np.exp(x) - 2
def f_1(x):
 return 3*(x**2) - 1 - np.exp(x) 
def f_2(x):
 return 6*x - np.exp(x) 
def secant():
  xn1 = 2
  xn = 3
  x = xn1
  while(abs(f(x)) > 0.00001):
    x = xn - ((f(xn) * (xn - xn1)) / (f(xn) - f(xn1)))
    xn1 = xn
    xn = x
  print("Root through Secant Method is {}".format(x))
def falsi():
  x_0=2
  x_1=3
  x_2= 5
  i=0
  while i < 20:
    x_2 = (x_0 * f(x_1) - x_1 * f(x_0))/ (f(x_1) - f(x_0)) 
    if f(x_2)==0:
      break
    if f(x_2)*f(x_0)<0:
      x_1=x_2
    else:
      x_0=x_2
    i=i+1
  print("Root through Regula-falsi Method is {}".format(x_2))
def newton():
  x_0=2
  x_1=3
  if abs(f(x_0))>=abs(f(x_1)):
    x_2=x_1
  else:
    x_2=x_0
  i=0  
  while i < 51:
    x_3 = x_2 - f(x_2)/f_1(x_2) 
    x_2=x_3
    i=i+1
  print("Root through Newton Raphson Method is {}".format(x_3))
def cheby():
  x_0=2
  x_1=3
  if abs(f(x_0))>=abs(f(x_1)):
    x_2=x_1
  else:
    x_2=x_0
  i=0  
  while i < 21:
    x_3 = x_2 - f(x_2)/f_1(x_2) - 0.5*(f(x_2)**2 / f_1(x_2)**3)*f_2(x_2)
    x_2=x_3
    i=i+1
  print("Root through chebyshev Method is {}".format(x_3))

while True:
  method= input("type 1 for Secant Method, 2 for Regula-falsi method, 3 for Newton Raphson method and 4 for Chebyshev method: ")
  if method=="1":
    secant()
  elif method=="2":
    falsi()
  elif method=="3":
    newton()
  elif method=="4":
    cheby()
  else:
    print("Invalid Entry")
  a=input("Enter Y for trying again. Anything else to exit: ")
  if a=="Y":
    continue
  else:
    break
