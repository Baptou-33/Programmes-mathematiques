n=int(input("Nombre premier n°"))
if n<0 or round(n)!=n:
    print("Nombre invalide")
elif n==1:
    print("Le 1 er nombre premier est 2")
else:
    nombres = [2]
    vérifiés = 3
    while len(nombres) < n:
        i = 0
        while i < len(nombres) and vérifiés % nombres[i] != 0:
            i += 1
        if i == len(nombres):
            nombres.append(vérifiés)
            if len(nombres)%1000==0 and n>1000:
                print(100*len(nombres)/n, "%")
        vérifiés += 2

    print("Le", n, "ième nombre premier est", nombres[-1])
