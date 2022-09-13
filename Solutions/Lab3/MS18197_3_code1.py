import numpy as np
def f(x):
  return np.cos(x)-x*np.exp(x)
def muller(a,b,c):
  c_before=100
  x = 200
  s=a
  t=b
  u=c
  while abs((x - c_before) / c_before ) > 0.0000001:
    c_before=c
    D= (c-b)*(c-a)*(b-a)
    a_1= ((f(c)-f(b))*((c-a)**2) - (f(c)-f(a))*((c-b)**2)) / D
    a_0= ((f(c)-f(b))*(c-a) - (f(c)-f(a))*(c-b)) / D
    a_2= f(c)
    if a_1 >= 0:
      x = c - 2*a_2 / (a_1 + (a_1**2 - 4*a_0*a_2)**0.5)
    else: 
      x = c - 2*a_2 / (a_1 - (a_1**2 - 4*a_0*a_2)**0.5)
    a=b
    b=c
    c=x
  print("The root for cos f(x)= cos(x) - x(e**x)is {} when initial guesses are ({},{},{})".format(c,s,t,u))
muller(-1,-2,-3),muller(-4,-6,-8)