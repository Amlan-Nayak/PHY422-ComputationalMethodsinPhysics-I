import numpy as np
from sympy import *
A= np.array([[ 15.,5.4772,0.,-0.,0.],[5.4772,66.3,96.5585,0.,-0.]
,[0.,96.5585, 282.6678,9.9845,-0.],[-0.,0.,9.9845,62.1587,40.6893]
,[0.,-0.,-0.,40.6893,59.8735]], dtype=float)
y = symbols('y')
sturm=[0 for i in range(A.shape[0]+1)]
sturm[0] = 1
sturm[1] = y - A[0,0]
for i in range(2,A.shape[0]):
  sturm[i] = (y - A[i,i])*sturm[i-1] - (np.round(A[i-2,i-1]**2,decimals=2))*sturm[i-2]
sturm[5] = (y - A[4,4])*sturm[4]  - (np.round(A[i-2,i-1]**2,decimals=2))*sturm[3]
while True:
  a=input("Enter guess: ")
  print("The signs of sturm sequences for the guess are:")
  print("1st = +ve")
  for i in range(1,A.shape[0]):
    j= np.sign(sturm[i].subs(y,float(a)))
    if j == 1:
      print ("+ve")
    else:
      print("-ve")
  b=input("Repeat with another guess(type Y for yes, N for no): ")
  if b == 'N':
    break
  else:
    pass
    