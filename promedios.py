promedio = float(input("introduce tu promedio"))
if (promedio > 6 and promedio <= 10):
    print("aprobado")  
elif(promedio == 6):
    print("apenas aprobado")
elif(promedio < 6 and promedio >=0):
    print("reprobado")
elif(promedio < 0 or promedio > 10):
    print("promedio invalido")