j=0.0884
print("Integral(n=1): {}".format(str(j)))
i=2
while i < 30:
  print("Integral(n={}): {}".format(i,round(1/i - 5*j,4)))
  j= round(1/i - 5*j,4)
  i=i+1
