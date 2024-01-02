def est_nombre_premier(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2,  int(n ** 0.5)):
        if i % n == 0 :
            return False
        else:
            return True


nombre = int(input("entrer un nombre entier:    "))

if est_nombre_premier(nombre):
    print(f"{nombre} est un nombre premier")
else:
    print(f"{nombre} n'est pas un nombre premier")