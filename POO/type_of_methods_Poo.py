# on a trois type de methose en POO les methodes static, les methode de classe et les methode d'instance
class Student:
    shoolName = "CDP"
    def __init__(self, french, english, math):
        self.french = french
        self.english = english
        self.math = math

    def average(self):
        return (self.math + self.french + self.english) / 3

# variable d instance: ascesseur et mutable Exeple

    def getMarkMath(self):
        return self.math

    def setMathMark(self, value):
        self.math = value

# methode de classe Exple
    def getShoolName(cls):
        return cls.shoolName
# methode static
    def info():
        print("CDP is a shit")
student1 = Student(15, 14, 16)
student2 = Student(16, 15, 18)

print(student1.average())
print(student2.average())
print(student1.getMarkMath()) # pour recuperer la note
student1.setMathMark(19)
print(student1.getMarkMath())
print(Student.shoolName)
Student.info()
