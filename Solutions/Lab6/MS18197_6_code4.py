import numpy as np
A= np.array([[1,1,1],[2,1,2],[1,3,2]], dtype=float)
A_copy= A
rows = A.shape[0]
for i in range(20):    
  U = np.zeros((rows, rows), dtype=float)
  L = np.eye(rows, dtype=float)   
  for k in range(rows):   
     U[k, k:] = A[k, k:] -  np.dot(L[k, :k] , U[:k, k:])
     L[(k+1):, k] = (A[(k+1):, k] -  np.dot(L[(k+1):, :]
, U[:, k])) / U[k, k]
  A = np.matmul(U,L)
print("Matrix") 
print(A_copy) 
print("The eigenvalues of the Matrix by Rutishauser method:")
print([np.round(A[i,i],decimals=5) for i in range(rows)])