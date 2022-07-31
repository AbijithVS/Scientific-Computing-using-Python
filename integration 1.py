import sympy as sp 
from scipy.integrate import quad

x=sp.Symbol('x')
print(sp.integrate(6.0*x**2+1,x))
def f(x):
   return 3.0*x**2+1
i=quad(f,1,2)
print(i[0])


