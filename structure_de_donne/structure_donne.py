# # les listes
# prenoms = ["albert", "awa", "joseph", "trump", "claude"]
#
# sub_prenoms = ["vincent", "émilie"]
# prenoms.extend(sub_prenoms)  # permet d'ajouter une liste dans une autre
# prenoms.insert(2, "Robert")  # permet d'ajouter un élément à un indice exact qu'on a précisé
# prenoms.remove("trump")  # permet de retirer un élément d'une liste
# prenoms.pop(3)  # il permet de retirer un élément à un indice précis par défaut, il retire le dernier élément
# # prenoms.clear()  # permet de vider la liste
# print(prenoms.index("awa"))  # permet de connaitre l'indice d'un élément
# print(prenoms.count("awa"))  # permet de savoir le nombre de fois qu'un élément apparait dans une liste
# prenoms.sort()  # permet d'ordonner une liste de façon ascendante
# prenoms.reverse()  # permet de reverser une liste
# a = prenoms.copy()
# print(a)

# matrice_transpose = []
# new = []
# for i in range(4):
#     for row in matrix:
#         new.append(row[i])
#     matrice_transpose.append(new)
#     new = []
#
# print(matrice_transpose)
# Liste exhaustive/ list comprehensive
#
# nombre = [x for x in range(10)]
# print(nombre)
# nombre2 = list(map(lambda x: x ** 2, range(10)))
# print(nombre2)
#
# # liste exhaustive à deux boucles
# listTuple = [(x, y) for x in [1, 2, 3, 4, 5] for y in [1, 2, 3, 4, 5] if x != y]
# print(listTuple)

# liste imbriquée
#
# matrix = [
#     [1, 5, 10, 15],
#     [2, 4, 6, 8],
#     [3, 6, 9, 12]
# ]
# matrix_t = [[row[i] for row in matrix] for i in range(4)]
# matrice_t2 = list(zip(*matrix))
# print(matrice_t2)
# print(matrix_t)

# tuples

tuple = 1, 2, 3, 4, 5, 6, 7, 8  # les tuples sont des listes qu'on ne peut pas modifier

# les ensembles


prenoms = set(["donald", "franc", "donald", "franc"])  # permet de créer une liste sans répétition des éléments
prenoms2 = {"donald", "mike", "sam"}

print(prenoms - prenoms2)  # permet d'obtenir tous les element de prenoms qui ne sont pas dans prenoms2
print(prenoms | prenoms2)  # permet d'obtenir la liste des prenoms qui sont dans prenoms ou dans prenoms2 sans
# répétition
print(prenoms ^ prenoms2)  # permet d'obtenir les élements qui sont soit dans prenoms soit dans prenoms2
# mais pas dans les deux
