nivel = int(input("escriba el nivel de la cisterna en metros:"))


if(nivel < 0 ):
    print("Fuga en la cisterna")
elif(nivel >= 0 and nivel <2 ):
    print("encienda la bomba de agua")
elif(nivel >=2 and nivel <4):
    print("la bomba esta trabajando")
elif(nivel>=4 and nivel <6):
    print("Desaceleré la bomba")
elif(nivel == 6 ):
    print("apague la bomba")
elif(nivel >6 ):
    print("desbordamiento")
