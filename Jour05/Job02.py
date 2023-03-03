def puissance(n):
    if n == 0:
        return n
    else:
        return n * n
n = int(input("Entrez un nombre: "))
if n == 0:
    print("Puissance de 0 est 0")
else:
    print(n, "puissance", n, "=", puissance(n))
