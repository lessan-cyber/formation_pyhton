# # fonction simple
# def somme_deux_nombre(a, b):
#     print(f"a est {a}")
#     print(f"b est {b}")
#     return a + b
#
#
# nombre1 = float(input("entrer a:  "))
# nombre2 = float(input("entrer b:  "))
# print(somme_deux_nombre(nombre1, nombre2))  # argument de position
#  print(somme_deux_nombre(a=nombre2, b=nombre1)) # argument avec mot clé
#

# fonction *args, **kwargs

def add_des_nombres(*args, **kwargs):
    i = 0
    for number in args:
        i += number
    for key in kwargs:
        print(kwargs[key])  # permet d'afficher la valeur contenue dans la clé e
    return i


# les args sont retournés sous forme de tuple, mais les kwargs sont retournés sous forme de dictionnaire
print(add_des_nombres(1, 2, 3, 5, 9, 7, 9, 6, 3))
# pour utiliser une liste deja faite, il faut
liste = [1, 12, 15, 84, 98, 65, 32]
# pour utiliser un dictionnaire déja fait, il faut
dictionnaire = {'a': 6, "b": 8, "c": 15, "d": 45}
print(add_des_nombres(*liste, **dictionnaire))  # l'étoile avant la variable liste permet de séparer les éléments de
# la liste ça s'appelle l'on packing

# EXPRESSION LAMBDA

exposant = lambda x, y: x ** 3 + y * 5  # permet d'écrire une fonction sur une seule ligne

print(exposant(2, 5))


def add_number():
    return lambda x: x ** 2


print(add_number()(5))  # ici, on ne passe pas la variable à la fonction add_number mais à son return


# documentation d'une fonction

def add():
    """
    documentation
    """
    pass


print(add.__doc__)  # permet de récupérer la documentation d'une fonction
