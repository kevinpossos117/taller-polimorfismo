### Taller de Polimorfismo — Python

Este proyecto demuestra el uso del polimorfismo en programación orientada a objetos mediante una jerarquía de clases que representan diferentes animales.
Cada clase implementa de forma distinta los métodos comunes hablar() y comer(), mostrando cómo el polimorfismo permite comportamientos diferentes según el tipo de objeto.

**Estructura del proyecto**

taller_polimorfismo

|

─ animales.py      # Clase base 'animales'

─ perro.py         # Subclase 'perro'

─ gato.py          # Subclase 'gato'

─ trex.py          # Subclase 'Trex'

─ main.py          # Archivo principal con el menú

---
### Concepto aplicado: Polimorfismo

El polimorfismo permite que distintas clases respondan de manera diferente al mismo método.
En este proyecto, todas las clases heredan de la clase base animales y redefinen los métodos hablar() y comer() con su propio comportamiento.

**Descripción de archivos**

animales.py: Contiene la clase base con los atributos generales y métodos comunes.
perro.py: Define la clase que representa a un perro y redefine los métodos hablar y comer.
gato.py: Define la clase que representa a un gato, con métodos para hablar, comer y ronronear.
trex.py: Define la clase que representa a un dinosaurio tipo T-Rex, con su propia versión de los métodos hablar y comer.
main.py: Contiene el menú principal que permite crear animales, ver la lista de los creados y ejecutar sus acciones.

---

## Funcionamiento del programa

El usuario puede interactuar con el programa mediante un menú en consola que ofrece las siguientes opciones:

Crear un perro

Crear un gato

Crear un T-Rex

Ver todos los animales creados

Salir del programa

**Ejecución**

Abrir la terminal en la carpeta del proyecto.

Ejecutar el archivo principal con el comando:

python main.py


Usar el menú para crear animales y observar cómo cada uno se comporta de forma diferente.

---

## Ejemplos de funcionamiento

Ejemplo de ejecucion de el de el menu 

<img width="923" height="315" alt="image" src="https://github.com/user-attachments/assets/7c733c56-4421-46ef-a088-32f375118304" />


Ejemplo al crear un animal y mostrar su comportamiento

<img width="934" height="317" alt="image" src="https://github.com/user-attachments/assets/49349ac3-8fc9-4afa-9fbf-f24fb22d44e0" />


Requisitos

Python 3.8 o superior

No se requieren librerías adicionales
