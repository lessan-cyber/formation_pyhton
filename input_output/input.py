file = open("data.txt")
print(file.read())  # permet de lire dans un fichier
# print(file)
file.close()

with open("data.txt") as f:  # avec la methode with on a pas besoin de fermer le fichier
    # print(f.read())
    first_line = f.readline()
    print(first_line)
    tell = f.tell()
    print(tell)

with open("data.txt", "a") as f:
    number = "aziz \n"
    f.write(str(number))



# les différents modes
# w : écriture dans un fichier vide
# r : lecture
# a : append permet d'écrire dans un fichier contenant deja du texte
# b: binaire

