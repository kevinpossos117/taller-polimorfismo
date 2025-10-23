class animales:
    def __init__(self, especie, edad, nombre):
        self.especie= especie
        self.edad= edad
        self.nombre= nombre

    def comer(self):
        print("el animal esta comiendo")
        
    def beber():
        print("el animal esta tomando agua")



class perro(animales):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)

    def ladrar(self):
        print("wao")

class gato(animales):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)

    def maullar(self):
        print("miau")
    
    def ronronear(self):
        print("grgrgrgrgr")

class Trex(animales):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)
    
    def rugir(self):
        print("graaaaaaa")


animal = perro("canino", 12, "gatazo")
print(animal.especie)
animal.ladrar()

animal2 = gato("felino", 6, "max")
print(animal2.especie)
animal2.ronronear()

rex = Trex("dinosaurio", 34, "princesa")
print("el animal se llama", rex.nombre, "y es de la especie",rex.especie)
rex.rugir()