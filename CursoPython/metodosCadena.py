nombreUsuario=input("Introduce tu nombre de usuario: ")

print ("El nombre es: ", nombreUsuario.upper()) #Convierte el texto en mayuscula

#-----------------------------------------------------------------------------


edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numerico")

edad=input("Introduce la edad: ")

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")