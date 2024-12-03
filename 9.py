import random
import string
import os



def mostrarMenu ():
    print("** MENU **")
    print("a) mostrar una lista de 3 servicios de pasaje con sus estrellas de calificacion")
    print("b) calcular la nomina de un empleado en enero del 2024")
    print("c) generar una contraseña con el numero de caracteres pedidos menor o igual a 5, si es mayor a 5 mostrar mensaje de error")
    print("d) Pedir al usario su nombre, primer ap., segundo ap. y edad e imprir un saludo con sus datos")


def lista_pasajes ():
    lista_transporte = []
    lista_calificacion = [] 
    for i in range(0,3):
        transporte = str(input("Transporte: "))
        lista_transporte.append(transporte)
        calificacion = int(input("Calificacion del 0 al 5: "))
        lista_calificacion.append(calificacion)
    lista_pasajes = lista_transporte, lista_calificacion
    print(lista_pasajes)

def calcular_nomina():
    dias = int(input("Dias trabajados: "))
    taxes = int(input("Cual es tu tasa de impuesto: "))
    salario_dia = int(input("Cuanto ganas al dia: "))
    salario = dias * salario_dia
    salario_neto = salario - (salario * (taxes / 100))
    print(f"Hola, trabajaste {dias} dias en Enero de 2024, por lo tanto tu sueldo sera el total de ${salario_neto}")

def generar_contrasena():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    n = int(input("Dame el numero de caracteres para generar tu contrasena: "))
    if (n <= 5):
        password = ''.join(random.sample(caracteres, n))
        print(password)
    else:
        print("Error, intentalo de nuevo")

def datos_persona():
    nombre = input("Dame tu nombre: ")
    apellido1 = input("Dame tu primer apellido: ")
    apellido2 = input("Dame tu segundo apellido: ")
    edad = input("Dame tu edad: ")
    print(f"Hola {nombre} {apellido1} {apellido2}, tienes {edad} años, te mando besitos bye :* :* ")



mostrarMenu() # invocar o mandar a llamar la funcion

opcion = input("Elige una opcion del menu: ")
if(opcion.lower() == "a" or opcion.lower() == "a)"):
    lista_pasajes()

elif(opcion.lower() == "b" or opcion.lower() == "b)"):
    calcular_nomina()

elif(opcion.lower() == "c" or opcion.lower() == "c)"):
    generar_contrasena()

elif(opcion.lower() == "d" or opcion.lower() == "d)"):
    datos_persona()

else:
    print("opcion no valida")
    mostrarMenu()