print("Programa de evaluacion de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
         valoracion = "suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))

#FUNCION INT -> Transforma en entero los parametros de la funcion input


