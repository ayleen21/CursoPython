edad=7

if 0< edad < 100: #Para que se valide,las dos condiciones deben ser correctas, si al ingresar al condicional alguna no se cumple se va al else
    print("La edad ingresada es correcta")
else:
    print("Edad incorrecta")

#----------------------------------------------------------

salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario de presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario de presidente: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del Jefe de Area: "))
print("Salario de presidente: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario administrativo: "))
print("Salario de presidente: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")