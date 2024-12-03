import random
import string
import os

def Mostrar_Menú():
  print("******** MENÚ *********")
  print("a) Mostrar una lista de 3 medios de transporte con sus estrellas de calificación")
  print("b) Calcular la nómina de un empleado en ENERO del 2024")
  print("c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error")
  print("d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos")

def Lista_Medios_Transporte():
  lista_pasajes = ["Metro", "Avión", "Metrobús"]
  lista_estrellas_calificación = [3, 4, 5]
  print(lista_pasajes, lista_estrellas_calificación)

def Calcular_Nómina():
  print("Nómina")

def Generar_Contraseña(número_caracteres):
  if(número_caracteres <= 5):
    # Definir los caracteres a utilizar
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(número_caracteres))
    return contraseña
  elif(número_caracteres > 5):
    return "ERROR"

respuesta = "si"

while(respuesta == "si" or respuesta == "SI" or respuesta == "Y" or respuesta == "S"):
  os.system('cls') # clear screen
  Mostrar_Menú() # Invocar o mandar a llamar la función
  opción = input("Elige una opción del menú: ")

  if(opción == "a" or opción == 'A' or opción == "a)" or opción == 'A)'):
    Lista_Medios_Transporte()
  elif(opción == "b" or opción == 'B' or opción == "b)" or opción == 'B)'):
    Calcular_Nómina()
  elif(opción == "c" or opción == 'C' or opción == "c)" or opción == 'C)'):
    x=(input("dame un numero"))
    Generar_Contraseña(x)
  elif(opción == "d" or opción == 'D' or opción == "d)" or opción == 'D)'):
    print("SALUDO")
  else:
    print("Opción no válida")

  respuesta = input("¿Quieres continuar?: ")