from sympy import *
x = symbols('x')
X = [1.2,2.1,2.8,4.1,4.9,6.2]
F = [4.2,6.8,9.8,13.4,15.5,19.6]
pol=0
for i in range(len(X)):
  a=1
  b=1
  for j in range(0,i):
    a = a*((x-X[j])/(X[i]-X[j]))
  for k in range(i+1,len(X)):
    b = b*((x-X[k])/(X[i]-X[k]))
  pol = pol + F[i]*a*b
print("x:",X)
print("f(x):",F)
print("The langrange interpolation polynomial is:")
print(simplify(pol))    
print("Value of interpolation polynomial at x=4.3 is",pol.subs(x,4.3))

#Here we use the bairstow method from Lab4
roots=[]
coef = Poly(pol-12,x).all_coeffs()
if len(coef)%2==0:
  while True:
    p=0.5
    q=1.9
    b=[1]
    c=[1]
    while abs(b[-1])>0.00005:
      b=[coef[0]]
      c=[coef[0]]
      b.append(coef[1]- p*b[0])
      c.append(b[1]- p*c[0])
      for i in range(2,len(coef)):
        b.append( coef[i]- b[i-1]*p- b[i-2]*q)
        c.append(b[i]- c[i-1]*p - c[i-2]*q)
      h1= - (b[-1]*c[-4]-b[-2]*c[-3])/(c[-3]**2 - c[-4]*(c[-2]-b[-2]))
      h2= - (b[-2]*(c[-2]-b[-2])-b[-1]*c[-3])/(c[-3]**2 - c[-4]*(c[-2]-b[-2]))
      p = p + h1
      q = q + h2
    roots.append( -p/2 + ((p**2-4*q)**0.5)/2)
    roots.append( -p/2 - ((p**2-4*q)**0.5)/2)
    coef=b[0:-2]
    if len(coef)==2:
      roots.append(-coef[1]/coef[0])
      break
    else:
      continue
else:
  while True:
    p=0.5
    q=0.9
    b=[1]
    c=[1]
    while abs(b[-1])>0.0000001:
      b=[coef[0]]
      c=[coef[0]]
      b.append(coef[1]- p*b[0])
      c.append(b[1]- p*c[0])
      for i in range(2,len(coef)):
        b.append( coef[i]- b[i-1]*p- b[i-2]*q)
        c.append(b[i]- c[i-1]*p - c[i-2]*q)
      h1= - (b[-1]*c[-4]-b[-2]*c[-3])/(c[-3]**2 - c[-4]*(c[-2]-b[-2]))
      h2= - (b[-2]*(c[-2]-b[-2])-b[-1]*c[-3])/(c[-3]**2 - c[-4]*(c[-2]-b[-2]))
      p = p + h1
      q = q + h2
    roots.append( -p/2 + ((p**2-4*q)**0.5)/2)
    roots.append( -p/2 - ((p**2-4*q)**0.5)/2)
    coef=b[0:-2]
    if len(coef)==3:
      roots.append( -coef[1]/(2*coef[0]) + ((coef[1]**2-4*coef[0]*coef[2])**0.5)/(2*coef[0]))
      roots.append( -coef[1]/(2*coef[0]) - ((coef[1]**2-4*coef[0]*coef[2])**0.5)/(2*coef[0]))
      break
    else:
      continue
roots= [N(i,5) for i in roots]
print("Roots at f(x)=12 are:")
print(roots)