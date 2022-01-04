from tkinter import * #Importar todas las clases de la libreria

raiz=Tk() #Raiz

raiz.title("Ventana de pruebas") #Titulo de la ventana

#El primer valor es el ancho width y el otro el alto height
#SI ponemos la raiz.resizable 0,0 no se podra modificar el tamaño de la ventana

#raiz.resizable(0,0) Admite parametros de ancho y alto, valor tipo boleano

#raiz.iconbitmap ("nombre de la imagen") ->Sirve para cambiar el icono de la ventana
  
#raiz.geometry("650x350") #Cambiar tamaño de la ventana

raiz.config(bg="purple") #COnfigurar color de la ventana

miFrame=Frame() #Construir frame 

miFrame.pack() #Empaquetar frame----------------------right->lo dirigo a la derecha bottom->A la parte inferior left->izquierda fill= x o y ->se expande

miFrame.config(bg="pink")

miFrame.config(width="650", height="350") #Eltamaño se le da al frame y no a la raiz, tiene un tamaño fijo

miFrame.config(bd=35) #Ponerle tamaño al borde

miFrame.config(relief="sunken") #Agregar borde

miFrame.config(cursor="pirate") #Configurar el cursos cuando este se posicione sobre el frame

raiz.mainloop() #Para que este en ejecucion debe estar en un bucle infinito, debe ir en ultimo lugar

#Con esto se crea la ventana

 