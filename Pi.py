import random

p = int(input("Précision : "))

def Monte_Carlo(n):
    bons_points = 0
    for i in range(n):
        x =random.uniform(0, 1)
        y =random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            bons_points += 1
        if i % 100000 == 0 and n> 100000:
            print(100*i/n, "%")
    return 4*bons_points/n

def Madhava_Leibniz(n):
    pi = 0
    for i in range(n):
        pi += ((-1)**i)/(1+2*i)
    return 4*pi

def John_Machin(n):
    pi = 0
    for i in range(n):
        pi += (((-1)**i)/(1+2*i))*((4/(5**(1+2*i)))-1/(239**(1+2*i)))
    return 4*pi

print(Monte_Carlo(p))
print(Madhava_Leibniz(p))
print(John_Machin(p))