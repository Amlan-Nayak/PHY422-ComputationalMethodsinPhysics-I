while True:
  coef = input("For the equation y= Ax^2 + Bx + C, enter values of A,B and C separated by commas: ")
  A= float(coef.split(",")[0])
  B= float(coef.split(",")[1])
  C= float(coef.split(",")[2])
  D= B**2 - 4*A*C
  if D >= 0:
    print("The equation is y= {}x^2 + {}x + {}".format(A,B,C))
    print("the roots are {} and {}".format((-B + D**0.5)/(2*A),(-B - D**0.5)/(2*A)))
  else:
    print("The equation is y= {}x^2 + {}x + {}".format(A,B,C))
    print("The roots are {} + {}i and {} - {}i".format(0.5*(-B/A),0.5*(((-D)**0.5)/A),0.5*(-B/A),0.5*(((-D)**0.5)/A)))
  a=input("Do you want to repeat? Press Y for yes, anything else for no: ")
  if a=="Y":
    continue
  else:
    break 