import numpy as np
from numpy.linalg import matrix_rank
A= np.array([[0,2,1,5],[4,1,-1,-3],[-2,3,-3,5]], dtype=float)
rows = A.shape[0]
for i in range(rows):
  A_copy= A.copy()
  #pivoting procedure
  maxi = A[:,i].tolist().index(max(A[:,i].tolist(),key=abs))
  if maxi > i:
    mid = A_copy[i,:]
    A[i,:]=A[maxi,:]
    A[maxi,:] = mid
  else:
    pass
  #making pivots 1 and starting elimination
  A[i,:]= A[i,:]/A[i,i]
  for j in range(i+1,rows):
    if A[j,i]!=0:
      A[j,:] =   A[j,:] -  A[j,i]*A[i,:]
    else:
      pass
#check rank for consistency
if matrix_rank(A) == matrix_rank(A[:,0:rows]):
#back substituition
  sol= np.zeros((rows,1))
  for i in range(rows-1, -1, -1):
    c = A[i,rows]
    for j in range(rows-1, i, -1):
        c = c - sol[j]*A[i,j]      
    sol[i] = c/A[i,i]
  print("The solutions are (" + str(["x"+str(i) for i in range(1,rows+1)]) 
  + "):",[float(i) for i in sol]) 
else:
  print("Equations not consistent")