import random

TAMANIO_CADENA = 13
GENES_POSIBLES = ' abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,.-;:_¿?¡!'
CADENA_OBJETIVO = "Industria 4.0"

class Gen:
    
    def __init__(self, cadena, tamanio, aptitud):
        self.cadena = cadena
        self.tamanio = tamanio
        self.aptitud = aptitud

def generar_lista_poblacion():
    print("Generando lista")
    poblacion = []
    for i in range(100):
        cadena = ''.join(random.choice(GENES_POSIBLES) for i in range(TAMANIO_CADENA))
        new_gen = Gen(cadena, TAMANIO_CADENA, 0)
        poblacion.append(new_gen)
        print(f"Gen: {new_gen.cadena}")
    return poblacion

# Devolvemos los 50 mejores
def devolver_genes_aptos(lista_poblacion):
    print("Devolviendo genes aptos")
    for gen in lista_poblacion:
        gen.aptitud = determinar_aptitud(gen.cadena)
    lista_poblacion.sort()

def determinar_aptitud(cadena):
    aptitud = 0
    ubicacion_string = 0
    for caracter in cadena:      
        if (caracter == CADENA_OBJETIVO[ubicacion_string]):
            aptitud = aptitud + 1
        ubicacion_string = ubicacion_string + 1
    return aptitud

def algoritmo_generico():
    lista_poblacion = generar_lista_poblacion()
    genes_aptos = devolver_genes_aptos(lista_poblacion)

    # while True:

algoritmo_generico()
