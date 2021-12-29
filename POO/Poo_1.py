#Propiedades



class Coche():
    
    def __init__(self): #Metodo constructor

        #con el self se agregan las propiedades al estado inicial

        self.largoChasis=250
        self.anchoChasis=120
        self.__Ruedas=4
        self.enmarcha=False #Por defecto el coche detenido

#----------------COMPORTAMIENTOS-------------------
    def arrancar(self,arrancamos): #-->Objeto perteneciente de la clase
        self.enmarcha=arrancamos

        if(self.enmarcha):
            chequeo=self.chequeointerno()

        if(self.enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.enmarcha and chequeo==False):  
            return" Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche esta parado"
            
    def estado(self):
        print("El coche tiene " , self.__Ruedas, " ruedas. Un ancho de ", self.anchoChasis, "y un largo de ",self.largoChasis)

    def chequeointerno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
#---------------------------------------------------------------------
miCoche=Coche() #Instancia

print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", self.__Ruedas " ruedas")

print(miCoche.arrancar(True))

miCoche.estado()

print ("-----------------A continuacion creamos el segundo objeto--------------------")

miCoche2=Coche()

print (miCoche2.arrancar(False))
miCoche2.estado()

