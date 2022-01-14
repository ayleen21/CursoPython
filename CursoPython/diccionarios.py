#nos permite almacenar dato de diferente tipo
#Cada dato tiene asociado una clave unica
#No importa el orden de los elementos
#Van dentro de llaves

midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}

print(midiccionario["Francia"])

print(midiccionario)

#Añadir nuevo elemento

midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Cambiar el valor

midiccionario["Italia"]="Roma"
print(midiccionario)

#ELiminar elemento //Se usa el metodo del

del midiccionario["Reino Unido"]
print(midiccionario)

#Asignar valores de una tupla

mitupla =["España", "Francia", "Reino Unido","Alemania"]
diccionario2={mitupla[0]:"Madrid", mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccionario)

#Visualizar elemento especifico
print(midiccionario["Francia"])

#Almacenar tupla en el diccionario y subdiccionario
midicc={23:"Jordan", "Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midicc["Anillos"])






