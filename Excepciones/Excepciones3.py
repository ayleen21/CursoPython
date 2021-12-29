def evaluacion(edad):

    if edad<0:
        raise MipropioError("No se perrmiten entradas negativas")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven
    elif edad<65: 
        return "ERES MADURO"
    elif edad<100: 
        return "Cuidate..."

print(evaluacion(-15))