from sympy import N
coef = [1,-3,-15,22,-30,-30,180]
roots=[]
while True:
    p=0.5
    q=0.9
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
    if len(coef)==3:
      roots.append( -coef[1]/(2*coef[0]) + ((coef[1]**2-4*coef[0]*coef[2])**0.5)/(2*coef[0]))
      roots.append( -coef[1]/(2*coef[0]) - ((coef[1]**2-4*coef[0]*coef[2])**0.5)/(2*coef[0]))
      break
    else:
      continue
roots = [N(i,5) for i in roots]
print("Roots are:")
for i in roots:
	print (i)