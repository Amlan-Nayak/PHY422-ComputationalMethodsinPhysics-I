import numpy as np
A=np.array([[-2,0,-1],[1,-1,1],[2,2,0]],dtype=float)
rows=A.shape[0]
v= np.random.rand(3,1)
y=1
eigen=1
for i in range(20):
  v_before=v.copy()
  y = np.matmul(A,v)
  v = y/max(abs(y))
print("The matrix:")
print(A)
eig = np.round(np.max(np.abs(y/v_before)),decimals=3)
#sign check
if np.abs(np.linalg.det(A - eig*np.eye(rows))) < 10**(-5):
  print("max eigenvalue is: ",eig)
  print("eigenvector is: ",np.round(v.T,decimals=3))
else: 
  print("max eigenvalue of A is: ",-eig)
  print("eigenvector is: ",np.round(v.T,decimals=3))