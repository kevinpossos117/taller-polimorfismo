from animales import animales

class Trex(animales):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)

    def hablar(self):
        print(f"{self.nombre} dice: graaaaaaa")

    def comer(self):
        print(f"{self.nombre} mastica triceratops")
