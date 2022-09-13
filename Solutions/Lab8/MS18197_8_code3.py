from sympy import *
X = [1,2,3,4,5]
F = [30,15,32,18,25]
h= X[1]-X[0]
m1,m2,m3,x = symbols('m1,m2,m3,x')
eq1= 4*m1 + m2 - 6*(F[0] - 2*F[1] + F[2])
eq2= m1 + 4*m2 + m3 - 6*(F[1] - 2*F[2] + F[3])
eq3= 4*m2 + m3 - 6*(F[2] - 2*F[3] + F[4])
M= list(solve([eq1,eq2,eq3],(m1,m2,m3)).values())
function = (((X[2] - x)**3)*M[0])/6  + (((x - X[1])**3)*M[1])/6 + (X[2] - x)*(F[1] - M[0]/6) + (x - X[1])*(F[2] - M[1]/6 )
print("x:",X)
print("f(x):",F)
print("The function through cubic spline method in interval (2,3) is ",simplify(function))
print("The function's value at x=2.5 is",function.subs(x,2.5))