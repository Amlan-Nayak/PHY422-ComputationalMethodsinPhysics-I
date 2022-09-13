import numpy as np
print("Check associative laws for X= 5.7834242, Y=0.0531451, Z=5.9898978")


while True:
  X= 5.7834242
  Y=0.0531451
  Z=5.9898978
  i= input("Type A for single precision and B for double precision: " )
  if i=='B':
    print("In double precision:")
    print("(X+Y)+ Z = X + (Y+Z) is {}".format((X+Y)+ Z== X+ (Y+Z)))
    print("(X*Y)*Z = X*(Y*Z) is {}".format((X*Y)*Z == X* (Y*Z)))
    print("X*(Y+Z)= X*Y + X*Z is {}".format(X*(Y+Z) == (X*Y)+ (X*Z)))
    print("(X+Y)- Z = (X-Z) + Y is {}".format((X+Y)- Z== (X-Z) +Y))
    print("X*(Y-Z) = X*Y - X*Z is {}".format(X*(Y-Z)==X*Y-X*Z))
  else:
    X= np.single(X)
    Y=np.single(Y)
    Z=np.single(Z)
    print("In single precision:")
    print("(X+Y)+ Z = X + (Y+Z) is {}".format((X+Y)+ Z== X+ (Y+Z)))
    print("(X*Y)*Z = X*(Y*Z) is {}".format((X*Y)*Z == X* (Y*Z)))
    print("X*(Y+Z)= X*Y + X*Z is {}".format(X*(Y+Z) == (X*Y)+ (X*Z)))
    print("(X+Y)- Z = (X-Z) + Y is {}".format((X+Y)- Z== (X-Z) +Y))
    print("X*(Y-Z) = X*Y - X*Z is {}".format(X*(Y-Z)==X*Y-X*Z))
  a=input("Do you want to repeat? Press Y if yes. Anything else for no.: ")
  if a=='Y':
    continue
  else:
    break