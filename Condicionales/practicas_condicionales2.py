print ("Programa de becas año 2017")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario familiar en bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a becas")