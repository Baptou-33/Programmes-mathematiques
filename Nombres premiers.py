from math import sqrt

p=[2,3]

def premier(n):
    if n<1 or round(n)!=n:
        return "Nombre invalide"

    k = p[-1]
    while len(p) < n:
        k += 2
        i = 0
        while p[i] <= sqrt(k) and k % p[i] != 0:
            i += 1
        if p[i] > sqrt(k):
            p.append(k)

    return p[n-1]

while True:
    print(premier(int(input("Nombre premier n°"))))