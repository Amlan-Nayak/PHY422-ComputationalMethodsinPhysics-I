import numpy as np
A= np.array([[2,1,4],[8,-3,2],[4,11,-1]], dtype=float)
B=np.array([12,20,33],dtype=float)
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
    #making pivots 1 and starting elimination
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
def mat_mul(A,B): #Multiplies two matrix
  C= np.zeros(shape=(A.shape[0],B.shape[1]),dtype=float)
  for i in range(0,A.shape[0]):
    for j in range(0,B.shape[1]):
      a= A[i,:]*B[:,j]
      sum=0
      for k in a:
        sum = sum + k
      C[i,j]= sum
  print(C) 
mat_mul(inverse(U,rows),inverse(L,rows)) #inverse of U,L multiplied