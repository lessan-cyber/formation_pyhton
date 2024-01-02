ages = {
    "donald": 20,
    "Samuel": 33,
    "aziz": 120,
    "joseph": 45
}  # premiere methode de création de dictionnaire les clé sont uniques


print(ages)

ages = dict([("aziz", 120), ("lessan", 454), ("metchonou", 69)])  # deuxième façon de déclarer un dictionnaire
print(ages)
print(ages["donald"])  # permet de sélectioner l'élément dont la clé est donald
