for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end=" ") #Indica como finalizar la expresion, todo se ejecuta en una sola linea con un espacio

#---------------------------------------------------------------------------
#Validacion email

contador=0
miEmail= input("Introduce tu correo electronico: ")

for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
        

if contador==2:
    print("Email es correcto")
else:
    print("El email no es correcto")

#-----------------------------------------
#TIpo range
for i in range(5,50,3): #Va a contar desde el 5 hasta un numero antes y si se agrega otro numero indicariamos de cuanto en cuanto queremos que empiece a correr
    print(f"valor de la variable {i}")

#Funcion len -> Devuelve la longitud en un string

valido=False 

email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("El email es correcto")
else:
    print("Email incorrecto")