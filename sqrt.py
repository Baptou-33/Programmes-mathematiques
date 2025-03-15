from math import *
from decimal import *
from decimal import Decimal as D

def sqrt(n, p):
    k = 10**D(n).log10().__floor__()
    sqrt = D(0)
    while not sqrt**D(2) == n and k > 10**(-D(p)-D(2)):
        print(round(100*D(k).log10()/D(10**(-D(p)-D(2))).log10()),"%")
        if sqrt**D(2) < n:
            while sqrt**D(2) <= n:
                sqrt += k
                if sqrt + k == sqrt:
                    print("Maximum atteint")
                    return sqrt
            sqrt -= k
        else:
            while sqrt**D(2)>= n and sqrt >= D(0):
                print("-")
                sqrt -= k
            sqrt += k
        k /= D(10)
    if sqrt**D(2) == n:
        return sqrt
    else:
        return round(sqrt, p)

a = int(input("Racine carrée de :"))
assert a >= 0
b = int(input("Nombre de décimales :"))
assert b >= 1
print(sqrt(a, b))