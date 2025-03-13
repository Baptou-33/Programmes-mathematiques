from random import *
from math import *
import decimal
from decimal import Decimal as D

p = int(input("Précision : "))
decimal.getcontext().prec = p

def Monte_Carlo(n):
    bons_points = 0
    for i in range(n):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if D(x)*D(x) + D(y)*D(y) <= D(1):
            bons_points += 1
    return D(4)*D(bons_points)/D(n)

def Madhava_Leibniz(n):
    pi = D(0)
    for i in range(n):
        pi += D(-1)**D(i)/(D(1)+D(2)*D(i))
    return D(4)*pi

def Riemann(n):
    pi = D(0)
    for i in range(1, n):
        pi += D(1)/D(i)**D(2)
    return D(D(6)*pi).sqrt()

def Wallis(n):
    pi = D(1)
    for i in range(1,n):
        pi *= D(4)*D(i)**D(2)/((D(2)*D(i)-D(1))*(D(2)*D(i)+D(1)))
    return D(2)*pi

def Archimede(n):
    a = D(4)
    b = D(8).sqrt()
    for i in range(n):
        a *= D(2)*b/(a+b)
        b = D(a*b).sqrt()
    return (a+b)/D(2)

def John_Machin(n):
    pi = D(0)
    for i in range(n):
        pi += D(-1)**D(i)/(D(1)+D(2)*D(i))*(D(4)/D(5)**(D(1)+D(2)*D(i))-D(1)/D(239)**(D(1)+D(2)*D(i)))
    return D(4)*pi

def Gauss_Legendre(n):
    a = D(1)
    b = D(1)/D(2).sqrt()
    p = D(1)
    t = D(0.25)
    for i in range(1, n):
        a, b, p, t = (a+b)/D(2), D(a*b).sqrt(), D(2)*p, t-p*((a+b)/D(2)-a)**D(2)
    return (a+b)**D(2)/(D(4)*t)

print("Monte-Carlo :    ", Monte_Carlo(p))
print("Madhava-Leibniz :", Madhava_Leibniz(p))
print("Riemann :        ", Riemann(p))
print("Wallis :         ", Wallis(p))
print("Archimède :      ", Archimede(p))
print("John Machin :    ", John_Machin(p))
print("Gauss Legendre : ", Gauss_Legendre(p))
