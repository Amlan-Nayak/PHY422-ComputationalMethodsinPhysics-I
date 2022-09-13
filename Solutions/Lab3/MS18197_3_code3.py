import numpy as np
def f(x):
  return x**3 + x**2 - 1
def p(x):
  return 1/(1+x)**0.5
def iteration(x):
  i=1
  while i < 20:
    y = p(x)
    x = y
    i=i+1
    if f(x)==0:
      break
    else: 
      continue   
  print ("Root of x**3 + x**2 - 1 by iteration method is {}".format(round(y,4)) )
def aitken(x):
  a=0
  b=0
  c=5
  while abs(c - 2*b + a)>0.0001:
    a=x
    b=p(x)   
    c=p(b)
    d= a - ((b - a)**2)/(c - 2*b + a)
    x = d
    if f(x)==0:
      break
    else: 
      continue   
  print ("Root of x**3 + x**2 - 1 by aitken's method is {}".format(round(d,4))) 
def f1(x):
  return x - np.exp(-x)
def p1(x):
  return np.exp(-x)
def iteration1(x):
  i=1
  while i < 20:
    y = p1(x)
    x = y
    i=i+1
    if f1(x)==0:
      break
    else: 
      continue   
  print ("Root of x - e**(-x) by iteration method is {}".format(round(y,4)) )
def aitken1(x):
  a=0
  b=0
  c=5
  while abs(c - 2*b + a)>0.0001:
    a=x
    b=p1(x)   
    c=p1(b)
    d= a - ((b - a)**2)/(c - 2*b + a)
    x = d
    if f1(x)==0:
      break
    else: 
      continue   
  print ("Root of x - e**(-x) by aitken's method is {}".format(round(d,4)))
iteration(2)
aitken(2)
iteration1(2)
aitken1(2)
