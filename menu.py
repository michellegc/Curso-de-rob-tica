from persona import Persona

nombre = input("Ingrese nombre aquí: ")
apellidos = input("Ingrese apellidos aquí: ")
sexo = input("Ingrese sexo de la persona aquí: ")
altura = input("Ingrese altura de la persona aquí: ")
color_ojos = input("Ingrese color de ojos de la persona aquí: ")
color_cabello = input("Ingrese color de cabello de la persona aquí: ")
edad = input("Ingrese la edad aquí: ")

persona = persona (nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello)
persona.mostrar_info()