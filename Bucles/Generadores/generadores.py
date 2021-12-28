def generaPares(limite):

    num=1

    while num<limite:

        yield num*2
      

        num=num+1

devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")

#-----------------------------------------
#Instruccion yield from

def devuelve_ciudades(*ciudades):
     for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))