n = int(input("Therme n°"))
if n<0 or round(n)!=n:
    print("Nombre invalide")
elif n==1:
    print("Le 1 er nombre premier est 1")
else:
    Fibonacci = [1,1]
    while len(Fibonacci)<n:
        Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
    print("Le", n, "ième therme de la suite de Fibonacci est", Fibonacci[-1])