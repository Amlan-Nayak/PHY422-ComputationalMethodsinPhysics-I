import matplotlib.pyplot as plt
import numpy as np
A=np.array([[4,1,1],[0,2,1],[-2,0,9]],dtype=float)
List=[A[i,i] for i in range(A.shape[0])]
Rad1= [sum(abs(A[i,:]))-abs(A[i,i]) for i in range(A.shape[0])]
Rad2= [sum(abs(A[:,i]))-abs(A[i,i]) for i in range(A.shape[0])]
fig, (ax1,ax2,ax3) = plt.subplots(3, 1,figsize=(15,15))
custom_xlim = (1,11)
custom_ylim = (-5, 5)
plt.setp(ax1, xlim=custom_xlim, ylim=custom_ylim)
plt.setp(ax2, xlim=custom_xlim, ylim=custom_ylim)
plt.setp(ax3, xlim=custom_xlim, ylim=custom_ylim)
ax1.axis('square')
ax2.axis('square')
ax3.axis('square')
ax1.set_xlabel('Real Axis')
ax1.set_ylabel('Complex Axis')
ax2.set_xlabel('Real Axis')
ax2.set_ylabel('Complex Axis')
ax3.set_xlabel('Real Axis')
ax3.set_ylabel('Complex Axis')
ax1.set_title('Row Circles')
ax2.set_title('Columns Circles')
ax3.set_title('Combined Row and Column Circle')
ax1.grid(),ax2.grid(),ax3.grid()
for i in range(len(List)):
    circle1 = plt.Circle((List[i], 0),radius = Rad1[i],color='r', alpha=0.3 )
    circle2 = plt.Circle((List[i], 0),radius = Rad2[i],color ='g', alpha=0.3)
    ax1.add_artist(circle1)
    ax2.add_artist(circle2)
for i in range(len(List)):
    circle1 = plt.Circle((List[i], 0),radius = Rad1[i],color='r',alpha=0.1 )
    circle2 = plt.Circle((List[i], 0),radius = Rad2[i],color ='g', alpha=0.1)
    ax3.add_artist(circle1)
    ax3.add_artist(circle2)    
plt.savefig('Task 1 First Matrix.png', dpi=300)