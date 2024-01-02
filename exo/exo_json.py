import json

continu = True
listeCourse = []
while continu:
    item_name = str(input("entrer le nom de votre produit:  "))
    item_price = int(input("entrer le prix de votre produit:    "))
    new_item = (item_name, item_price)
    listeCourse.append(new_item)

    choix = str(input("voulez vous continuez(oui ou non):   "))
    if choix == "oui":
        continu = True
    else:
        continu = False

with open("listeCourse.json", "x") as f:
    json.dump(listeCourse, f)
