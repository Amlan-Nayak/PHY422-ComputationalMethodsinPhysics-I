import numpy as np
A= np.array([[2,4,1,3],[3,2,-2,-2],[3,-3,3,18]], dtype=float)
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
  if i>0:
    for k in range(i):
      A[k,:] =   A[k,:] -  A[k,i]*A[i,:]
  else:
    pass
print("The solutions are (" + str(["x"+str(i) for i in range(1,rows+1)])
+ "): ",[round(i,4) for i in A[:,rows]]) 
