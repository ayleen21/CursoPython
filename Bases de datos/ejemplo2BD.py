import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#Se usan estas comillas cuando la instruccion sera muy larga
miCursor.execute('''                    
           CREATE TABLE PRODUCTOS (
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
           PRECIO INTEGER,
           SECCION VARCHAR(20))
 ''')

productos=[
    
    ("Pelota",20,"Jugueteria"),
    ("Pantalon",15,"Confeccion"),
    ("Destornillador",25,"ferreteria"),
    ("Jarron",45,"Ceramica"),
    ("Pantalones",35,"Confeccion")
    
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)



miConexion.commit()

miConexion.close()