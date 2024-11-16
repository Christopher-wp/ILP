#operaciones matematicas 

#DECLARAR O CREAR VARIABLES O CONSTANTES 
nombre_completo = "Christopher Chong "
edad = 33
estatura = 1.82
direccion = "calle x , colonia y"
telefono = "55 11545121"
correo = "tote@mx.com"
activo = True
#CONSTANTE
PI = 3.1416
GRAVEDAD = 9.81



##### se le llama importar librerias o bliblotecas que contienen funciones
import math
#### asi se importan librerias 
dato1 = float(input("ingrese un dato:"))
dato2 = float(input("ingrese un dato:"))

suma= dato1 + dato2 
print("el resultado de la esuma es=",suma)
resta = dato1 - dato2 
print("el resultado de la resta es ",resta)
multiplicacion = dato1 * dato2 
print ("el resultado de la multiplicacion es ",multiplicacion)
divicion = dato1/dato2
print ("el resultado de divicion es ",divicion)
potencia = dato1 ** dato2
print("el resultado de la potencia  es ",potencia)
cuadrado = dato1 ** 2
print ("el resultado de elevar al cuadrado es ",cuadrado)
potencia2 = pow(dato1,dato2)
print("el resultado de la potencia del numero 1 elevado al numero 2 es :", potencia2)
raiz_cuadrada = math.sqrt(16)
print("la raiz cuadrada de 16 es=:",raiz_cuadrada)
raiz_cuadrada2 = pow(16,1/2)
raiz_cubica = pow(27,1/3)
modulo_residuo_1 = 10 % 2
modulo_residuo_2 = dato1 % dato2
print('modulo 1 residuo es =',modulo_residuo_1)
print("modulo 2 residuo es=", modulo_residuo_2)