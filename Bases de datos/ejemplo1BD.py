import sqlite3   #Importar libreria sqlite

miConexion=sqlite3.connect("PrimeraBD") #Crear conexion y dar nombre a la BD

miCursor=miConexion.cursor() #Crear cursor o puntero

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))") #Se debe comentar la linea en cuanto se ejecute una vez porque si no saldra un error, con este codigo se crea la tabla

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
""" 
variosProductos=[ #Ingresar varios registros, se crea una lista
    
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camion",20,"Jugueteria")
    
    
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)  """#Insertar la lista con los registros, los signos de interrogacion depende de cuantos campos tenga la tabla

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall() #Nos devuelve una lista con todos los productos, para poder verlos necesitamos almacenar la lista en una variable

for producto in variosProductos: #Visualizar productos mediante un ciclo
    print ("Nombre Articulo: ",producto[0], " Seccion: ", producto[2])
    
    
miConexion.commit() #Se usa para confirmar los cambios en la tabla













miConexion.close() #Cerrar BD
