for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end=" ") #Indica como finalizar la expresion, todo se ejecuta en una sola linea con un espacio

#---------------------------------------------------------------------------
#Validacion email

email = False
miEmail= input("Introduce tu correo electronico: ")

for i in miEmail:
    if(i=="@"):
        email = True

if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")