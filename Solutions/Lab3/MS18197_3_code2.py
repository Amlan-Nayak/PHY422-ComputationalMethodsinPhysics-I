import numpy as np
def f(x):
  return x**3- 13*x - 12
def f1(x):
  return 3*(x**2) - 13
def multipoint1(x):
  x_ini=x
  x_2= 200
  x_before=300
  while abs((x_2 - x_before)/x_before) > 0.00000001:
    x_before=x
    y = x - 0.5*(f(x)/f1(x))
    x_2 = x - f(x)/f1(y)
    x = x_2
    if f(x)==0:
      break
    else:
      continue
  print("The root closest to {} of f(x) = x**3 - 13x - 12 is {} by first multipoint method".format(x_ini,x_2))
def multipoint2(x):
  x_ini=x
  x_2= 200
  x_before=300
  while abs((x_2 - x_before)/x_before) > 0.00000001:
    x_before=x
    y = x - f(x)/f1(x)
    x_2 = y - f(y)/f1(x)
    x = x_2
    if f(x)==0:
      break
    else:
      continue
  print("The root closest to {} of f(x) = x**3 - 13x - 12 is {} by second multipoint method".format(x_ini,x_2))
multipoint1(5)
multipoint1(-11)
multipoint1(1)
multipoint2(5)
multipoint2(-11)
multipoint2(1)