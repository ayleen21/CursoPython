 import pickle

    lista_nombres=["Perdon","Ana","Maria", "Isabel"]

 #Dar nombre al fichero externo  
    fichero_binario=open("lista_nombres","wb")  
#wb ->estructura binaria

        pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
