from math import *
from decimal import *
from decimal import Decimal as D

p = int(input("Nombres de décimales : "))
getcontext().prec = p+3
a = D(1)
b = D(1)/D(2).sqrt()
c = D(1)
d = D(0.25)
for i in range(1, ceil(log(p)*4)):
    a, b, c, d = (a+b)/D(2), D(a*b).sqrt(), D(2)*c, d-c*((a+b)/D(2)-a)**D(2)
    print(floor(100*i/ceil(log(p)*4)), '%')
print(D((a+b)**D(2)/(D(4)*d)).quantize(D(10)**(-p), rounding=ROUND_DOWN))
