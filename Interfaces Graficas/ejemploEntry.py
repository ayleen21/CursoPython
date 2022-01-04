from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar() #Indicar que se trata de una cadena de caracteres

cuadroNombre=Entry(miFrame,textvariable=minombre) #Poner el cuadro de texto, textvariable lo usamos para asociar esa variable
#cuadroTexto.place(x=100, y=100)empaquetar cuadro de texto indicando su ubicacion
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="purple",justify="center") #Modificacion del color del texto, y de la ubicacion

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=4, column=1,padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview) #Agregar barra de desplazamiento, se indica en que widget se desea poner y yview ->Vertical
scrollVert.grid(row=4,column=2,sticky="nsew") #asignar la ubicacion de la barra,nsew->Conseguir que se adapte la barra al tamaño del widget

textoComentario.config(yscrollcommand=scrollVert.set) #El posicionador se acomoda dependiendo del tamaño del texto

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e", padx=10,pady=10) #Ubicacion del label

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10) 

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():

    minombre.set("Juan") #Set->Establecer valor a una variable

botonEnvio=Button(raiz, text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()