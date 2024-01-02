# il existe dux type de variable en Poo il a les variable d'instance et les variable de classe
class Car:
    def __init__(self):
        self.engine = "Diesel"
        self.mark = "BMW"
        # les variable d'instance sont déclarés dans le init
    wheels = 4  # on declare les variable de classe hors du init

car1 = Car()
car2 = Car()
Car.wheels = 5  # pour changer une variable de classe on la modigie grace à la classe
print(car1.engine, car1.mark , car1.wheels)
print(car2.engine, car2.mark, car2.wheels)