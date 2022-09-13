import numpy as np
print("Find root of equation for f(x)=8 - 4.5(x-sin(x)) using bisection method")

def f(x):
 return 8 - 4.5*(x-np.sin(x))
coef= input("enter two different lower and upper bound for the solution[A,B](mod(A) should not be mod(B)): ")
up=float(coef.split(",")[1])
low=float(coef.split(",")[0])
if f(up)*f(low)>0:
  print("Invalid entries. Enter again")
  coef= input("enter two different lower and upper bound for the solution[A,B](mod(A) should not be mod(B)): ")
  up=float(coef.split(",")[1])
  low=float(coef.split(",")[0])
elif f(up)*f(low)==0:
  if f(up)==0:
    print("The value of root is : {} ".format(up))
  else:
    print("The value of root is : {} ".format(low))

mid = 1
mid_before=10

while abs(mid-mid_before)/abs(mid) > 0.001: 
        mid_before=mid 
        mid = (up+low)/2 
        if (f(mid) == 0.0): 
            break
        elif (f(mid)*f(low) < 0): 
            up = mid 
        else: 
            low = mid 
        
              
print("The value of root is : {} ".format(mid)) 