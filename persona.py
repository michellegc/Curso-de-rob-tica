class Persona:
    def __init__(self,nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.color_ojos = color_ojos
        self.color_cabello = color_cabello
        
    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellidos)
        print("Color de cabello: " + self.color_cabello)
        print("Altura: " + self.altura)
        print("Sexo: " + self.sexo)
        print("Edad: " + self.edad)
        #Etc...
        
        
    def mostrar_edad(self):
        edad = int(self.edad)
        edad = edad + 10
        print("En diez años "+self.nombre + " tendra: " +str(edad))
        
#pepito = Persona("José","Camilo santos","Hombre","12","1.56","negro","negro")
#pepito.mostrar_info()
#pepito.mostrar_edad()

nombre = input("Ingrese nombre aquí: ")
apellidos = input("Ingrese apellidos aquí: ")
sexo = input("Ingrese sexo de la persona aquí: ")
altura = input("Ingrese altura de la persona aquí: ")
color_ojos = input("Ingrese color de ojos de la persona aquí: ")
color_cabello = input("Ingrese color de cabello de la persona aquí: ")
edad = input("Ingrese la edad aquí: ")

persona = Persona (nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello)
persona.mostrar_info()
persona.mostrar_edad()


                
        
        