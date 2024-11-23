edad = int(input("introduce tu edad"))

if (edad >= 18 and edad <= 120):    #rango valido 18 hasta 120
 print("MAYOR DE EDAD")
elif(edad == 0 or edad <= 17):      #rango valido de 0 a 17
 print("menor de edad")
elif(edad < 0 or edad >120 ):
    print("edad no valida")                 #valores no validos
 
