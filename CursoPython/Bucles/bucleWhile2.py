#Hacer que el bucle no sea infinito
import math #Las clases de python para poder usarse deben importarse

print("Programa de calculo de raiz cuadrada")

numero=int(input("Introduce un numero por favor: "))

intentos=0 #Inicializar variable en 0

while numero <0:
    print("No se puede hallar la raiz de un numero negativo")

    if(intentos==2):
        print("Has realizado demasiados intentos, el programa finalizara.")
        break
    
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero) #Retorna la raiz cuadrada de un numero
    print ("La raiz cuadrada de " + str(numero) + " es " + str(solucion))