import random
import textdistance
from time import sleep

TAMANIO_CADENA = 13
GENES_POSIBLES = ' abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,.-;:_¿?¡!'
CADENA_OBJETIVO = "Industria 4.0"
PORCENTAJE_APTOS_NECESARIA_INICIAL = 0.5
PORCENTAJE_MAS_APTOS = 0.2

class Cromosoma:
    
    def __init__(self, genes, tamanio):
        self.genes = genes
        self.tamanio = tamanio
        self.aptitud = None
        self.identificador = hash(self.genes)
        if (genes == CADENA_OBJETIVO):
            self.es_cromosoma_ideal = True
        else:
            self.es_cromosoma_ideal = False
        self.determinar_aptitud_eficiente()

    def determinar_aptitud(self):
        ubicacion_gen = 0
        for gen in self.genes:      
            if (gen == CADENA_OBJETIVO[ubicacion_gen]):
                self.aptitud = self.aptitud + 1
            ubicacion_gen = ubicacion_gen + 1
        print(f"Cromosoma: {self.genes} ------>  Aptitud: {self.aptitud}")

    def determinar_aptitud_eficiente(self):
        self.aptitud = textdistance.hamming.normalized_similarity(self.genes, CADENA_OBJETIVO)
        print(f"Cromosoma: {self.genes} ------>  Aptitud: {self.aptitud}")

def generar_lista_poblacion():
    print("Generando lista")
    poblacion = []
    for i in range(100):
        cadena = ''.join(random.choice(GENES_POSIBLES) for i in range(TAMANIO_CADENA))
        new_cromosoma = Cromosoma(cadena, TAMANIO_CADENA)
        poblacion.append(new_cromosoma)
    return poblacion

def devolver_numero_aptos_segun_porcentaje(lista, porcentaje):
    numero_poblacion = len(lista)
    nuemro_necesario = int(numero_poblacion * porcentaje)
    return nuemro_necesario

# Devolvemos los 50 mejores
def devolver_cromosomas_aptos(lista_poblacion, porcetaje_aptos_necesaria):
    print("Devolviendo cromosomas aptos")
    lista_poblacion.sort(key=lambda x: x.aptitud, reverse=True)
    numero_lista_aptos_necesaria = devolver_numero_aptos_segun_porcentaje(lista_poblacion, porcetaje_aptos_necesaria)
    lista_aptos = lista_poblacion[:numero_lista_aptos_necesaria]
    return lista_aptos

def generar_proxima_generacion(lista_cromosomas_aptos, porcentaje_mas_aptos):
    print("Generando proxima generacion")
    numero_lista_aptos_necesaria = devolver_numero_aptos_segun_porcentaje(lista_cromosomas_aptos, porcentaje_mas_aptos)
    lista_proxima_generacion = lista_cromosomas_aptos[:numero_lista_aptos_necesaria] # ya tenemos el 10%

def algoritmo_genetico():
    cromosoma_ideal = Cromosoma('', TAMANIO_CADENA)
    lista_poblacion = generar_lista_poblacion()
    lista_cromosomas_aptos = None
    lista_proxima_generacion = None
    while cromosoma_ideal.es_cromosoma_ideal == False:
        sleep(3)
        lista_cromosomas_aptos = devolver_cromosomas_aptos(lista_poblacion, PORCENTAJE_APTOS_NECESARIA_INICIAL)  # 50% aptos
        lista_poblacion = generar_proxima_generacion(lista_cromosomas_aptos, PORCENTAJE_MAS_APTOS)
        cromosoma_ideal = filter(lambda x: x.genes == CADENA_OBJETIVO, lista_poblacion)
        #cromosoma_ideal.val
    # print(cromosoma_ideal)

algoritmo_genetico()
