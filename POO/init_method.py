class Computer:
    def __init__(self, cpu, ram, hdd ):  # constructeur on peut aussi donner des valeur par défaut au attribut exple hdd = "500GB"
        print("je suis dans le init")
        self.mycpu = cpu
        self.myram = ram
        self.myhdd = hdd
    def compare(self, other):
        return self.mycpu == other.mycpu

    def configuration(self):
        print(f" configuration: {self.mycpu , self.myram, self.myhdd}")
    def modify_cpu(self, new_cpu):
        self.mycpu = new_cpu

computer1 = Computer("E5", "4BG","1TB")
computer2 = Computer("E7","32GB", "2TB")
computer1.configuration()

if computer1.compare(computer2):
    print("computer1 est egale a computer2 en cpu")
else:
    print("computer1 n'est pas egale a computer2 en cpu")