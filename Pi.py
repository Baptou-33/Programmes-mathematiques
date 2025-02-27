from random import *
from math import *

p = int(input("Précision : "))

def Monte_Carlo(n):
    bons_points = 0
    for i in range(n):
        x =uniform(0, 1)
        y =uniform(0, 1)
        if x**2 + y**2 <= 1:
            bons_points += 1
    return 4*bons_points/n

def Madhava_Leibniz(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i/(1+2*i)
    return 4*pi

def John_Machin(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i/(1+2*i)*(4/5**(1+2*i)-1/239**(1+2*i))
    return 4*pi

def Riemann(n):
    pi = 0
    for i in range(1, n):
        pi += 1/i**2
    return sqrt(6*pi)

def Gauss_Legendre(n):
    a = 1
    b = 1/sqrt(2)
    p = 1
    t = 0.25
    for i in range(1, n):
        a_new = (a+b)/2
        b_new = sqrt(a*b)
        p_new = 2*p
        t = t-p*(a_new-a)**2
        a = a_new
        b = b_new
        p = p_new

    return (a+b)**2/(4*t)

def Wallis(n):
    pi = 1
    for i in range(1,n):
        pi *= 4*i**2/((2*i-1)*(2*i+1))
    return 2*pi

if p <= 1024:
    print(Gauss_Legendre(p))
else:
    print(Gauss_Legendre(1024))
print(Monte_Carlo(p))
print(Madhava_Leibniz(p))
print(Riemann(p))
print(Wallis(p))
if p < 11:
    print(John_Machin(p))
else:
    print(John_Machin(11))