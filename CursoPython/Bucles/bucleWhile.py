i=1

while i <=10:
    print("Ejecucion " + str(i))
    i=i+1

print("Termino la ejecucion")

#------------------------------------

edad=int(input("Introduce tu edad por favor: "))

while edad<0:
    print("Has introducido una edad negativa.Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: " + str(edad))

#Bucle while con operadores logicos

edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta.Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: " + str(edad))