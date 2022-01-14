#Sintaxis de las funciones

def mensaje(): #Declarando la funcion
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones basicas en python")
    print("Poco a poco iremos avanzando")

mensaje() #Llamando la funcion

   
print("Ejecutando codigo fuera de funcion")
mensaje()

def suma():
    num1=5
    num2=7
    print(num1+num2)  


suma() 


#Usar la misma funcion con otros valores

   
def sumar(nu1,nu2):
    print(nu1+nu2)



sumar(6,7) 


sumar(2,1) 


sumar(8,9)

#Usar return

def sum(n1,n2):
    resultado =n1+n2

    return resultado 

print(sum(5,7))

almaneca_resultado =sum(300,200)

print(almaneca_resultado)
