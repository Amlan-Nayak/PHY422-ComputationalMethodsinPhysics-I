import numpy as np
A= np.array([[10,-2,-1,-1],[-2,10,-1,-1],[-1,-1,10,-2],
[-1,-1,-2,10]],dtype=float)
B= np.array([[3],[15],[27],[-9]],dtype=float)
rows= A.shape[0]
X = np.ones((1,rows),dtype=float) 
X1 = np.zeros((1,rows),dtype=float)
k=1
while np.sum(np.abs(X-X1)[:]) > 0.001:
  X1=X.copy()
  for i in range(rows):
    sum1 = np.sum(np.subtract(np.dot(A[i,:],X.T),A[i,i]*
X[0,i]))
    X[0,i] = (B[i] - sum1)/(A[i,i])
  k=k+1
print("For the given system of equations:")
print("A=")
print(A)
print("B=")
print(B)
print("The roots through Gauss Stridel method are:")
print([float(np.round(i,decimals=3)) for i in X[0,:]])
print("Number of Iterations:" ,k)