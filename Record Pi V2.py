from math import *
from decimal import *
from decimal import Decimal as D

p = int(input("Nombres de décimales : "))
getcontext().prec = p+3
profondeur = 0

def binary_split(a, b, profondeur):
    if b == a + 1:
        Pab = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
        Qab = 10939058860032000 * a ** 3
        Rab = Pab * (545140134 * a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m, profondeur + 1)
        Pmb, Qmb, Rmb = binary_split(m, b, profondeur + 1)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    print(profondeur)
    return Pab, Qab, Rab

def chudnovsky(n):
    P1n, Q1n, R1n = binary_split(1, n, 1)
    print("Derniers calculs...")
    pi = D(10005).sqrt()
    print("2/10")
    pi *= Q1n
    print("5/10")
    pi *= 426880
    print("6/10")
    pi /= 13591409 * Q1n + R1n
    print("10/10\n\nCalculs terminés! Pi est environ égal à :")
    return pi

print(D(chudnovsky(max(ceil(p/14), 2))).quantize(D(10)**(-p), rounding=ROUND_DOWN))