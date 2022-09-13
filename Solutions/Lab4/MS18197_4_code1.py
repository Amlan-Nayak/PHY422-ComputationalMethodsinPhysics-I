coef= [3,20,-10,-240,-250,200]
roots=[]
while True:
  p=0.5
  b=[1]
  while abs(b[-1])>0.00005:
    b=[coef[0]]
    c=coef[0]
    for i in range(1,len(coef)):
      b.append(b[i-1]*p + coef[i])
      if i < len(coef)-1:
        c = b[i] + c*p
    p = p - b[-1]/c
  roots.append(p)
  coef=b[0:-1]
  if len(coef)==1:
    break
  else:
    continue
roots = [round(i,4) for i in roots]
print("The roots are: ")
for i in roots:
	print(i)