import numpy as np
A = np.random.rand(20,20)
B = A[:10,:10]
E = A[10:,10:]
D = A[10:,:10]
C = A[:10,10:]
I_1= np.eye(10)
I_2=np.eye(10)
def inv(a,rows): #inverse of a matrix
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
def Inverse(b):
  rows = b.shape[0]
  U = np.zeros((rows, rows), dtype=float)
  L = np.zeros((rows, rows), dtype=float)   
  for k in range(rows):  
        L[k, k] = b[k, k] - np.dot( L[k, :] , U[:, k])  
        U[k, k:] = (b[k, k:] -  np.dot(L[k, :k] , U[:k, k:])) / L[k, k]
        L[(k+1):, k] = (b[(k+1):, k] -  np.dot(L[(k+1):, :], U[:, k])) / U[k, k]
  return np.matmul(inv(U,rows),inv(L,rows))
B_Inv = Inverse(B)
V = np.matmul(Inverse(E - np.matmul(np.matmul(D,B_Inv),C)),I_2)
Z = - np.matmul(np.matmul(V ,D ), B_Inv)
Y =  - np.matmul( B_Inv,np.matmul(C ,V ))
X = np.matmul(B_Inv, I_1 - np.matmul(C,Z))
A_Inv = np.zeros((20,20))
A_Inv[:10,:10] = X 
A_Inv[10:,10:] = V
A_Inv[10:,:10] = Z
A_Inv[:10,10:] = Y


print("The Matrix:")
print(np.round(A,decimals= 3))
print("The Inverse")
print(np.round(A_Inv,decimals=3))
print ("The Matrix * The Inverse")
print(np.round(np.matmul(A,A_Inv),decimals=3))