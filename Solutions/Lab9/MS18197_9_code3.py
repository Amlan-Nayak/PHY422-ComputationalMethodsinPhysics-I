import numpy as np
X = np.linspace(0,84,num=15)
Y = [124,134,148,156,147,133,121,109,99,85,78,89,104,116,123]

print("Time in secs:",X)
print("Speed in  km/secs:",Y)
h = X[1] - X[0]

print("\nUsing Trapezoidal rule:")
value = 0.5*h*(Y[0]+Y[-1] + 2*np.sum(Y[1:-1:1]))
print(" Length of track in kms:", np.sum(value))

print("\nUsing Simpson 1/3 rule:")
value = (h/3)*(Y[0]+Y[-1] + 4*np.sum(Y[1:-1:2])+2*np.sum(Y[2:-2:2]))
print(" Length of track in kms:", np.sum(value))

print("\nUsing Simpson 3/8 rule:")
value = (3*h/8)*(Y[0]+Y[-1]  + 2*np.sum(Y[3:-1:3]))
for i in range(3,len(Y),3):
  Y[i] = 0
value = value +(3*h/8)*3*np.sum(Y[1:-1])
print(" Length of track in kms:", np.sum(value))