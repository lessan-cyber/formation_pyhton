liste = ["a", "b", "c"]
try:
    for element in liste:
        print(element)
except NameError:  # pour une exception particuliere
    print("desole une de vos variable n est pas defini")
except Exception as e:  # pour gérer toutes les exceptions
    print(e)
else:
    print("exécution complète")