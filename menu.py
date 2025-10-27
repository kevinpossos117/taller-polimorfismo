from perro import perro
from gato import gato
from trex import Trex

def menu():
    animales_lista = []

    while True:
        print("MENÚ DE ANIMALES")
        print("1. Crear perro")
        print("2. Crear gato")
        print("3. Crear Trex")
        print("4. Ver todos los animales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del perro: ")
            edad = int(input("Edad: "))
            especie = "canino"
            nuevo = perro(especie, edad, nombre)
            animales_lista.append(nuevo)
            print(f"\nHas creado un perro llamado {nombre}")
            nuevo.hablar()
            nuevo.comer()

        elif opcion == "2":
            nombre = input("Nombre del gato: ")
            edad = int(input("Edad: "))
            especie = "felino"
            nuevo = gato(especie, edad, nombre)
            animales_lista.append(nuevo)
            print(f"\nHas creado un gato llamado {nombre}")
            nuevo.hablar()
            nuevo.comer()

        elif opcion == "3":
            nombre = input("Nombre del Trex: ")
            edad = int(input("Edad: "))
            especie = "dinosaurio"
            nuevo = Trex(especie, edad, nombre)
            animales_lista.append(nuevo)
            print(f"\nHas creado un Trex llamado {nombre}")
            nuevo.hablar()
            nuevo.comer()

        elif opcion == "4":
            print("LISTA DE ANIMALES")
            if not animales_lista:
                print("No hay animales creados aún.")
            else:
                for a in animales_lista:
                    print(f"{a.nombre} ({a.especie}, {a.edad} años)")
                    a.hablar()
                    a.comer()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
