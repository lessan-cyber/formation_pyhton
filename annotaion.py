# les annotations permettent de donner plus d'info sur une variable, le type de retour d'une fonction

def add_number(a: str, b: str, c: int) -> str:  # cette ligne veut dire que a et b sont des strings, c est un entier
    # et que la fonction retourne un string
    return a + b


print(add_number("aziz", "lawson", 3))

print(add_number.__annotations__)  # permet de récupérer les annotations d'une fonction
