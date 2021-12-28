#Instrucciones continue

nombre="Pildoras informaticas"

contador=0

for i in nombre:
    if i==" ":
        continue #Esta funcion hace que se salte el espacio y no lo cuente
    contador+=1

print(contador)

#Instrucciones pass

class MiClase:
    pass #Para implemenmtar mas tarde 

#Instruccion Else

email=input("Por favor,ingrese su correo electronico: ")

for i in email:
      if i=="@":
          arroba=True

          break

else:
    arroba=False

print(arroba)


