"""
print("Hello World")
"""
# les conditions

nombre1, nombre2 = 22, 15

if nombre1 > nombre2:
    print("cool")
else:
    print("pas cool")  # condition simple

if nombre1 == 10:
    print("c est 10")

elif nombre1 == 15:
    print("c est 15")
elif nombre1 == 25:
    print("c est 25")
else:
    print("I don't know what is it")  # condition multiple

# LES BOUCLES

nombre_paires = [2, 4, 7, 6, 8, 10]

for nombre in nombre_paires:  # pour chaque nombre de la liste nombre_paires
    exposant = nombre ** 2
    print(nombre)

paire = True

i = 2

while paire:
    print(i)
    if i % 2 != 0:
        paire = False
    i += 1  # incrémentation décrémentation i-= 1

# Break and continue

print("-----------------------------------------------")

for nombre in nombre_paires:
    if nombre % 2 != 0:
        continue  # permet de ne pas exécuter le reste du code si une condition n'est pas remplie, mais de reprendre
        # directement la boucle
    print(nombre)

for nombre in nombre_paires:
    if nombre % 2 != 0:
        break  # permet de sortir d'une boucle dès qu'une condition n'est pas verifier
    print(nombre)

# types de variables

number1, number2, success, name = 2, 2.2, True, "Donald"

print(type(number1))
print(type(number2))
print(type(success))
print(type(name))

# Formatage de variables
nom = input("quelle est ton s appelle")
print("bonjour ", nom)
print("bonjour {}".format(nom))  # avec cette methode, le nombre d'accolades est égale au nombre de variables

