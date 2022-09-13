import numpy as np
#A= np.array([[2,-3,1],[1,2,-3],[4,-1,-2]], dtype=float)
A= np.array([[2,1,4],[8,-3,2],[4,11,-1]], dtype=float)
B=np.array([12,20,33],dtype=float)
rows = A.shape[0]    
U = np.zeros((rows, rows), dtype=float)
L = np.zeros((rows, rows), dtype=float)   
for k in range(rows):  
        L[k, k] = A[k, k] - np.dot( L[k, :] , U[:, k])  
        U[k, k:] = (A[k, k:] -  np.dot(L[k, :k] , U[:k, k:])) / L[k, k]
        L[(k+1):, k] = (A[(k+1):, k] -  np.dot(L[(k+1):, :], U[:, k])) / U[k, k]

sol= np.zeros((rows,1))
for i in range(rows):
    c = B[i]
    for j in range(i):
        c = c - sol[j]*L[i,j]      
    sol[i] = c/L[i,i]
for i in range(rows-1, -1, -1):
    c = sol[i]
    for j in range(rows-1, i, -1):
        c = c - sol[j]*U[i,j]      
    sol[i] = c
print("The solutions through Crout method are ("
+str(["x"+str(i) for i in range(1,rows+1)])+"):"
,[float(i) for i in sol])