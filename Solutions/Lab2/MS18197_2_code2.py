print("Find root of equation for f(x)=x^3 - 3x + 1 on [0,1] using bisection method")
up=1
low=0
def f(x):
  return x**3 - 3*x + 1
mid= 1
mid_before=10
while abs(mid-mid_before)/abs(mid) > 0.001: 
  mid_before=mid 
  mid=(low+up)/2
  if f(mid)==0:
      break
  elif f(mid)*f(low)>0:
    low= mid
  else:
    up=mid
    
print("The value of root is : {} ".format(mid))