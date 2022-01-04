from tkinter import *

root=Tk()

miFrame=Frame(root, width=1000, height=1000)

miFrame.pack()

miImagen=PhotoImage(file="girasol.gif") #Nos permite manipular imagen

#miLabel=Label(miFrame, text="Hola alumnos de python", fg="blue", font=("Comic Sans MS",18)) Agregar texto al label
#miLabel.pack() #Para que se muestre en pantalla el texto
Label(miFrame, image=miImagen).place(x=100, y=200) #Este metodo nos permite ubicar el texto en cualquier parte de la interfaz, mediante coordenadas 










root.mainloop()
