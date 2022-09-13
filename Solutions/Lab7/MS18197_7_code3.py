import numpy as np
A= np.array([[2,-1,0],[-1,2,-1],[0,-1,2]], dtype=float)
rows = A.shape[0]   
U = np.zeros((rows, rows), dtype=float)
L = np.zeros((rows, rows), dtype=float)   
for k in range(rows):  
        L[k, k] = A[k, k] - np.dot( L[k, :] , U[:, k])  
        U[k, k:] = (A[k, k:] -  np.dot(L[k, :k] , U[:k, k:])) / L[k, k]
        L[(k+1):, k] = (A[(k+1):, k] -  np.dot(L[(k+1):, :], U[:, k])) / U[k, k]
def inverse(a,rows): #inverse of a matrix
  D=np.zeros((rows,2*rows),dtype=float)
  D[:,:rows]=a
  D[:,rows:]=np.eye(rows,dtype=float)
  D_copy=D.copy()
  for i in range(rows):
    D_copy= D.copy()
    D[i,:]= D[i,:]/D[i,i]
    for j in range(i+1,rows):
      if D[j,i]!=0:
        D[j,:] =  D[j,:] -  D[j,i]*D[i,:]
      else:
        pass
    if i>0:
      for k in range(i):
        D[k,:] =   D[k,:] -  D[k,i]*D[i,:]
    else:
      pass
  return D[:,rows:] 
A_inv = np.matmul(inverse(U,rows),inverse(L,rows))
v= np.random.rand(3,1)
y=1
eigen=1
for i in range(20):
  v_before=v.copy()
  y = np.matmul(A_inv,v)
  v = y/max(abs(y))
print("The matrix A is: ")
print (A)
if np.abs(np.linalg.det(A - (1/max(y))*np.eye(3))) < 10**(-5):
  print("min eigenvalue of A is: ",(1/max(y)))
else: 
  print("min eigenvalue of A is: ",(-1/max(y)))