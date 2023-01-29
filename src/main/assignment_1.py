from numpy import* 
import struct
#Question 1
int_data = int('0100000001111110101110010000000000000000000000000000000000000000',2)
double_data = struct.unpack('d', struct.pack('q', int_data))[0]
print(double_data,"\n")

#Question 2
chop = int(double_data)
print(chop,"\n")

#Question 3
round_data= round(double_data)
print(round_data,"\n")

#Question 4
absolute_error = (round_data-double_data)
print(absolute_error,)

relative_error = (absolute_error / double_data)
print(relative_error,"\n")

#Question 5
def infinite_series(x, k:float):
  return((-1)**k) * ((x**k)/(k**3))
function=1
itteration=1
while(abs(infinite_series(function, itteration)) > 10**-4):
  itteration += 1

print(itteration-1,"\n")

#Question 6
import numpy as np

def my_bisection(f, a, b, tol): 
   
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) <tol:
        return 0
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)+1
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)+.75
f = lambda x: (x**3) + (4* (x**2)) - 10


print(my_bisection(f, -4, 7, .0001))

def my_newton(f, df, x0, tol):
    x=x0
    if abs(f(x0)) > tol:
        return x0
    else:
        return my_newton(f, df, x0 -f(x0)/df(x0), tol)
f = lambda x:  (x**3) + (4* (x**2)) - 10
df= lambda x: 3 * (x**2) + (8 * x)
print(my_newton(f,df,7,.0001))
    
