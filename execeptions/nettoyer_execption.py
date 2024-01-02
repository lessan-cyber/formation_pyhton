# permet d'ignorer une execption ou d'exécuter un bout de code peu import l'execption

try:
    for element in [0, 1, 2, 3, 4, 5, 6]:
        print(element)
except Exception as e:
    print(e)
else:
    print("aucune exception")
finally:
    print("peut importe on y va quand meme") 