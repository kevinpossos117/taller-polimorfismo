from animales import animales

class gato(animales):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)

    def hablar(self):
        print(f"{self.nombre} dice: miau")

    def ronronear(self):
        print("grgrgrgrgr")

    def comer(self):
        print(f"{self.nombre} come atún enlatado")
