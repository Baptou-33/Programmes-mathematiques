from math import *
from decimal import *
from decimal import Decimal as D

def sqrt(n, g, p):
    k = 10**D(n).log10().__floor__()
    g = D(g)
    sqrt = D(0)
    while not sqrt**g == n and k > 10**(-D(p)-D(2)):
        if sqrt**g < n:
            while sqrt**g <= n:
                sqrt += k
                if sqrt + k == sqrt:
                    print("\nMaximum atteint (27 décimales)")
                    return sqrt
            sqrt -= k
        else:
            while sqrt**g >= n and sqrt >= D(0):
                print("-")
                sqrt -= k
            sqrt += k
        k /= D(10)
    if sqrt**g == n:
        return sqrt
    else:
        return round(sqrt, p)

a = int(input("Racine de :"))
assert a >= 0
b = int(input("Racine combien-ième ? "))
assert b >=1
c = int(input("Nombre de décimales :"))
assert c >= 1
print("\nsqrt(", a, ",", b, ") = ", sqrt(a, b, c))