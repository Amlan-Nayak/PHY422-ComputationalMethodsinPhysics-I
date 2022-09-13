import numpy as np
x= np.pi/3
a=np.pi/4
taylor= np.sin(a)+np.cos(a)*(x-a)- (np.sin(a)*((x-a)**2))/2 - (np.cos(a)*((x-a)**3))/6 
print("Value of sin(x) at x=pi/3 is {}".format(np.sin(x)))
print("Taylor series expansion of sin(x) about pi/4 is {}".format(taylor))
print("Difference between both is {} % ".format(abs(((-taylor + np.sin(np.pi/3))/np.sin(np.pi/3))*100)))