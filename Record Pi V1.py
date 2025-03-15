from math import *
from decimal import *
from decimal import Decimal as D

p = 10**9 #max = 999999999999999999
getcontext().prec = p

print("Initialisation")
a = D(1)
print("1/100")
b = D(1)/D(2).sqrt()
print("98/100")
c = D(1)
print("99/100")
d = D(0.25)
print("100/100\nDébut des itérations")
for i in range(1, 60):
    a, b, c, d = (a+b)/D(2), D(a*b).sqrt(), D(2)*c, d-c*((a+b)/D(2)-a)**D(2)
    print(2**i, " : ", D((a+b)**D(2)/(D(4)*d)).quantize(10**-(2**i), rounding=ROUND_DOWN))
