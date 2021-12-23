#NO SE PUEDEN MODIFICAR DESPUES DE SU CREACION
#Las porciones que se extraen, su resultado se almacena en otra tupla
#Se puede comprobar si un elemento hace parte de la lista

mitupla=("Juan",30,12,2018)

print(mitupla[2])

#Metodos para convertir una tupla a lista
milista=list(mitupla)
print(milista)

#Metodo para convertir una lista a tupla

mitupla=tuple(milista)
print(milista)

print("Juan" in mitupla)
#Count ->Permite averiguar cuantos elementos se encuentran denttro de una tupla

print(mitupla.count(30))

#Len -> Nos dice cuantos elementos t enemos
print(len(mitupla))

#Tupla unitaria -> //Se debe poner la , despues del unico elemento

tuplaUnit=("Juan",)
print(len(tuplaUnit))

#Empaquetado de tuplas -> almacenar datos de tuplase en variables

nombre,dia, mes, año = mitupla
print(nombre)
print(dia)
print(año)
print(mes)

