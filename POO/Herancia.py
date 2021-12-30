class Vehiculos(): #Clase padre

    def __init__(self,marca,modelo): #Constructor

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False #Por defecto no esta en marcha
        self.acelera=False
        self.frena=False

#------------------------------COMPORTAMIENTOS-----------------
#Cambiar el estado de las propiedades del constructor

        def arrancar(self):

            self.enmarcha=True

        def acelerar(self):

            self.acelera=True

        def frenar(self):

            self.frena=True

        def estado(self):
            print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos): #Se pone entre parentesis el nombre de la clase padre
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
            print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class vElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

#Se hereda todo incluido el constructor
miMoto=Moto("Honda", "CBR") #Instancia, SE INCLUYE LA MARCA Y EL MODELO

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(vElectricos,Vehiculos): #Herencia multiple, siempre tiene preferencia la primera que se pone
    pass

miBici=BicicletaElectrica()



