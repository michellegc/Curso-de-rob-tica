class gato:
    def __init__(self,nombre,nombre_cien,tamanio,sexo,edad,peso):
        self.nombre = nombre
        self.nombre_cien = nombre_cien
        self.tamanio = tamanio
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
        
    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Nombre cientifico: " + self.nombre_cien)
        print("Tamaño: " + self.tamanio)
        print("Sexo: " + self.sexo)
        print("Edad: " + self.edad)
        print("Peso: " + self.peso)
        
nombre = input("Ingrese el nombre del gato: ")
nombre_cien = input("Ingrese el nombre cientifico del gato: ")
tamanio = input("Ingrese el tamaño del gato: ")
sexo = input("Ingrese el sexo del gato: ")
edad = input("Ingrese la edad del gato: ")
peso = input("Ingrese el peso del gato: ")

Gatos = gato (nombre,nombre_cien,tamanio,sexo,edad,peso)
Gatos.mostrar_info()
        