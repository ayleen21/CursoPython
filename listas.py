#Listas 
from typing import Pattern


miLista=["Maria", "Pepe", "Marta", "Antonio"]

#Imprimir todos los elementos de la lista

print(miLista)

#Imprimir elemento especifico

print(miLista[2])

#Imprimir porcion de lista = accede a algunos elementos
#Incluye los indices del 0 al 2, el  3 lo excluye

print(miLista[0:3])

#Comienzo del indice desde 1

print(miLista[1:3])

#Comienzo desde algun indice especifico hasta el final

print(miLista[2:])

#append -> Metodo para añadir nuevos elementos a la lista 

miLista.append("Sandra")

print(miLista[:])

#inser -> Metodo para añadir nuevos elementos a la lista, indicando su ubicacion

miLista.insert(2,"Luisa")

print(miLista[:])    
   

#extend -> Metodo para añadir varios eleemntos a la lista
# miLista.extend["Lucia", "Laura", "Camila"]


#index-> Nos ayuda a saber en que posicion esta el element

print(miLista.index("Antonio")) 
       
 #Mostrar si el elemento se encuentra en la lista //Responde true o false
   
print("Pepe" in miLista)

#Remove -> ELiminar elementos de la lista

miLista.remove("Maria")
print(miLista[:])

#Pop ->Elimina el ultimo elemento de la lista

miLista.pop()

print(miLista[:])

#Union de listas

miLista2=["Samantha", "Lina"]

result=miLista+miLista2

print(result[:])

# * -> Funciona como repetidor

miLista3=["Monica",6,True,21.80] * 3
print(miLista3[:])
