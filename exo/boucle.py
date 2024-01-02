listeCourse = []
code_valide = [["cdp20", 0.2], ["cdp50", 0.5], ["cdp70", 0.7]]
continu = True
while continu:
    nom = str(input("entrer le nom de l article:       "))
    prixArticle = float(input("entrer le prix de l article:     "))
    newArticle = [nom, prixArticle]
    print(newArticle)
    listeCourse.append(newArticle)
    choix = str(input("souhaitez vous continuez (oui ou non)"))

    if choix == "oui":
        continu = True
    else:
        continu = False
        codeReduction = str(input("entrer le code de réduction:     "))
        listeCourse.append(["codeReduction", codeReduction])


def appliquer_reduction(liste):
    somme = 0

    for i in range(len(listeCourse) - 1):
        somme += listeCourse[i][1]

    somme_avec_reduction = somme

    customer_code = liste[len(liste) - 1][1]
    for elt in code_valide:
        if customer_code == elt[0]:
            somme_avec_reduction = somme_avec_reduction * (1 - elt[1])

    if somme_avec_reduction == somme:
        print("votre code est invalide")
    return somme_avec_reduction


print(f"avec votre code de reduction "
      f"{listeCourse[len(listeCourse) - 1][1]}" 
      f" votre solde est de {appliquer_reduction(listeCourse)}")
