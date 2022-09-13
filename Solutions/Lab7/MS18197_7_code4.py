import numpy as np
A= np.array([[15,4,3,2,-1],[4,25,6,-7,8],[3,6,27,8,9],[2,-7,8,319,10],[-1,8,9,10,100]], dtype=float)
A_copy=A.copy()
rows = A.shape[0]
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
for i in range(0,rows-1):
  for j in range(i+1,rows-1):
    B= np.eye(5)
    theta = np.arctan(A[i,j+1]/A[i,i+1])
    B[i+1,i+1]= np.cos(theta)
    B[j+1,j+1]= np.cos(theta)
    B[i+1,j+1]= -np.sin(theta)
    B[j+1,i+1]= np.sin(theta)
    U = np.zeros((rows, rows), dtype=float)
    L = np.zeros((rows, rows), dtype=float)   
    for k in range(rows):  
        L[k, k] = B[k, k] - np.dot( L[k, :] , U[:, k])  
        U[k, k:] = (B[k, k:] -  np.dot(L[k, :k] , U[:k, k:])) / L[k, k]
        L[(k+1):, k] = (B[(k+1):, k] -  np.dot(L[(k+1):, :], U[:, k])) / U[k, k]
    B_inv = np.matmul(inverse(U,rows),inverse(L,rows))
    A = np.matmul(np.matmul(B_inv,A),B)
A = np.round(A,decimals=4)
print("The matrix:")
print(A_copy)
print("The tri-diagonal matrix by Given’s method:")
print(A)