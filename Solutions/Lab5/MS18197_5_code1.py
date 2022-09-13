import numpy as np
A= np.array([[1,2,3],[2,1,4],[1,4,3]],dtype=float)
B= np.array([[2,1],[1,2],[2,1]],dtype=float)
def mat_mul(A,B):
  if A.shape[1]==B.shape[0]:
    C= np.zeros(shape=(A.shape[0],B.shape[1]),dtype=float)
  else:
    print("incorrect dimensions")
  for i in range(0,A.shape[0]):
    for j in range(0,B.shape[1]):
      a= A[i,:]*B[:,j]
      sum=0
      for k in a:
        sum = sum + k
      C[i,j]= sum
  print(C)
mat_mul(A,B)