def union(conjunto1, conjunto2):
    resultado = list(conjunto1)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def interseccion(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento in conjunto2:
            resultado.append(elemento)
    return resultado

def diferencia(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.append(elemento)
    return resultado

def complemento(universo, conjunto):
    resultado = []
    for elemento in universo:
        if elemento not in conjunto:
            resultado.append(elemento)
    return resultado

def union3(conjunto1, conjunto2, conjunto3):
    resultado = list(conjunto1)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.append(elemento)
    for elemento in conjunto3:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def interseccion3(conjunto1, conjunto2, conjunto3):
    resultado = []
    for elemento in conjunto1:
        if elemento in conjunto2 and elemento in conjunto3:
            resultado.append(elemento)
    return resultado

def diferencia3(conjunto1, conjunto2, conjunto3):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2 and elemento not in conjunto3:
            resultado.append(elemento)
    return resultado

def complemento3(universo, conjunto1):
    resultado = []
    for elemento in universo:
        if elemento not in conjunto1:
            resultado.append(elemento)
    return resultado