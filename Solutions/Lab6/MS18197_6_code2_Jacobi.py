import numpy as np
A= np.array([[10,-2,-1,-1],[-2,10,-1,-1],[-1,-1,10,-2],
[-1,-1,-2,10]],dtype=float)
B= np.array([[3],[15],[27],[-9]],dtype=float)
rows= A.shape[0]
D,L,U= np.zeros((rows,rows)),np.zeros((rows,rows)),np.zeros((rows,rows)) 
for i in range(rows):
  D[i,i] = 1/A[i,i]
  for j in range(i+1,rows):
    L[j,i]=A[j,i]
    U[i,j]=A[i,j]
x0 = np.ones((rows,1),dtype=float)
x1 = np.zeros((rows,1))
i=1
while np.sum(np.abs(x0-x1)[:]) > 0.001:
  x1=x0.copy()
  x0 = x0 + np.matmul(D, B - np.matmul(A,x0))
  i=i+1
print("For the given system of equations:")
print("A=")
print(A)
print("B=")
print(B)
print("The roots through Jacobi method are:")
print([float(np.round(i,decimals=3)) for i in x0])
print("Number of Iterations:" ,i)