import numpy as np
A=np.array([[1,3,2,-1],[3,-3,2,4],[-4,2,5,1],[-1,2,-3,5]],dtype=float)
B= np.array([[9],[19],[27],[14]],dtype=float)
rows= A.shape[0]
D,L,U= np.zeros((rows,rows)),np.zeros((rows,rows)),np.zeros((rows,rows)) 
for i in range(rows):
  D[i,i] = A[i,i]
  L[i+1:rows,i] = A[i+1:rows,i]
  U[i,i+1:rows] = A[i,i+1:rows]
max_eigen=11 #spectral radius bound from Gerschgorin circles
if 1 - max_eigen**2 > 0:
  w = (2/(1+ (1 - max_eigen**2)**(1/2)))
else:
  w = (2/(1+ (-1 + max_eigen**2)**(1/2)))
x0 = np.ones((rows,1),dtype=float)
x1 = np.zeros((rows,1),dtype=float)
i=1
while np.sum(np.abs(x0-x1)[:]) > 0.00001:
  x1=x0.copy()
  x0 = x0 + np.matmul(np.linalg.inv(D+w*L),w*(B - np.matmul(A,x0)))
  i=i+1
print("For the given system of equations:")
print("A=")
print(A)
print("B=")
print(B)
print("For the given system of equations") 
print("The roots are: ",[float(np.round(i,decimals=4)) for i in x0])
print("Number of iterations:",i)
print("The value of relaxtion parameter:",np.round(w,decimals=3))