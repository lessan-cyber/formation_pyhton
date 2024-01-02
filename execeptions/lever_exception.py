# permet de créer nos propres exception si le variable ne sous pas notre logique
try:
    number = 1
    if number not in range(6):
        raise ValueError("votre nombre n est pas entre 1 et 5 ")  # l'exception
except Exception as e:
    print(e)
else:
    print("tout va bien")
