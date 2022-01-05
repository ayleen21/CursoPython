from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+="Ṕlaya"

    if(montana.get()==1):
        opcionEscogida+="Montana"

    if(turismoRural.get()==1):
        opcionEscogida+="Turismo rural"

    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="avion.gif")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elige destinos", width=50).pack()

Checkbutton(frame,text="Playa", variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montana",variable=montana,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje).pack()


textoFinal=Label(frame)
textoFinal.pack ()

root.mainloop()