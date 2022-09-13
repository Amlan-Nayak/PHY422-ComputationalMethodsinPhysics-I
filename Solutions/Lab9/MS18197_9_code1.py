import numpy as np
X = [0,25,50,75,100,125]
F =[0,32,58,78,92,100]
Y=F
Divide =[]
print("Time in secs=",X)
print("Distance in kms=",F)
print("\nDivided Difference table:")
for k in range(len(X)-1):
  Y = [np.round((Y[i+1]-Y[i])/(X[i+k+1]-X[i]),decimals=6) for i in range(len(Y)-1)]
  print("Difference number "+str(k+1)+" :", Y)
  Divide.append(Y[0])
def der(x):
  return Divide[0] +  Divide[1]*(2*x - X[0] - X[1]) 
print("\nValue of Velocity at:")
for k in range(len(X)):
  print("t="+str(X[k])+"secs:", np.round(der(X[k]),decimals=6))
print("\nValue of Velocity at:")
for k in range(len(X)):
  print("t="+str(X[k])+"secs:", 2*Divide[1])