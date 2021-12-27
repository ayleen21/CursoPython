num1=(int(input("Introduce el primer numero, por favor: ")))
num2=(int(input("Introduce el segundo numero, por favor: ")))

    
def DevuelveMax (num1,num2):
    if num1 > num2:
        print (num1)
    elif num1 < num2:
        print (num2)
    else:
        print ("Los numeros son iguales")

print ("El numero mayor es: ")

DevuelveMax (num1,num2)