import random
import textdistance
from time import sleep

TAMANIO_CADENA = 13
POBALCION = 100
GENES_POSIBLES = ' abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,.-;:_¿?¡!'
CADENA_OBJETIVO = "Industria 4.0"
PORCENTAJE_POBLACION_HIJOS = 0.9
PORCENTAJE_APTOS_NECESARIA_INICIAL = 0.5
PORCENTAJE_MAS_APTOS = 0.2

class Cromosoma:
    
    def __init__(self, genes, tamanio, genes_padre_1, genes_padre_2):
        self.genes = genes
        self.tamanio = tamanio
        self.aptitud = 0
        self.identificador = hash(self.genes)
        if (genes == CADENA_OBJETIVO):
            self.es_cromosoma_ideal = True
        else:
            self.es_cromosoma_ideal = False
        self.genes_aptos = []
        # self.determinar_aptitud_eficiente()
        self.genes_padre_1 = genes_padre_1
        self.genes_padre_2 = genes_padre_2
        self.determinar_aptitud()

    def determinar_aptitud(self):
        ubicacion_gen = 0
        for gen in self.genes:      
            if (gen == CADENA_OBJETIVO[ubicacion_gen]):
                self.aptitud = self.aptitud + 1
                self.genes_aptos.append(ubicacion_gen)
            ubicacion_gen = ubicacion_gen + 1
        print(f"Cromosoma: {self.genes} ------>  Aptitud: {self.aptitud} --- Genes padres:{self.genes_padre_1, self.genes_padre_2}")

    def determinar_aptitud_eficiente(self):
        self.aptitud = textdistance.hamming.normalized_similarity(self.genes, CADENA_OBJETIVO)
        print(f"Cromosoma: {self.genes} ------>  Aptitud: {self.aptitud}")

def generar_lista_poblacion():
    print("Generando lista")
    poblacion = []
    for i in range(POBALCION):
        cadena = ''.join(random.choice(GENES_POSIBLES) for i in range(TAMANIO_CADENA))
        new_cromosoma = Cromosoma(cadena, TAMANIO_CADENA, None, None)
        poblacion.append(new_cromosoma)
    return poblacion

def devolver_numero_necesario_segun_porcentaje(lista, porcentaje):
    numero_poblacion = len(lista)
    nuemro_necesario = int(numero_poblacion * porcentaje)
    return nuemro_necesario

# Devolvemos los 50 mejores
def devolver_cromosomas_aptos(lista_poblacion):
    print("Devolviendo cromosomas aptos")
    lista_poblacion.sort(key=lambda x: x.aptitud, reverse=True)
    numero_lista_aptos_necesaria = devolver_numero_necesario_segun_porcentaje(lista_poblacion, PORCENTAJE_APTOS_NECESARIA_INICIAL) # 50
    lista_aptos = lista_poblacion[:numero_lista_aptos_necesaria]
    return lista_aptos

def generar_proxima_generacion(lista_cromosomas_aptos, lista_poblacion):
    print("Generando proxima generacion")
    rango_mas_aptos = devolver_numero_necesario_segun_porcentaje(lista_cromosomas_aptos, PORCENTAJE_MAS_APTOS) # 10
    rango_lista_hijos = devolver_numero_necesario_segun_porcentaje(lista_poblacion, PORCENTAJE_POBLACION_HIJOS) # 90
    lista_proxima_generacion = lista_cromosomas_aptos[:rango_mas_aptos] # ya tenemos el 10%
    lista_hijos = reproducir_hijos(lista_cromosomas_aptos, rango_lista_hijos) # Otro 90%
    lista_proxima_generacion.extend(lista_hijos)
    lista_proxima_generacion.sort(key=lambda x: x.aptitud, reverse=True)
    return lista_proxima_generacion

def reproducir_hijos(lista_cromosomas_aptos, rango_lista_hijos):
    lista_hijos = []
    for i in range(rango_lista_hijos):
        cromosoma_padre_1 = lista_cromosomas_aptos[random.randrange(len(lista_cromosomas_aptos))]
        cromosoma_padre_2 = lista_cromosomas_aptos[random.randrange(len(lista_cromosomas_aptos))]
        lista_hijos.append(mutacion(cromosoma_padre_1, cromosoma_padre_2))
    return lista_hijos

def mutacion(cromosoma_padre_1, cromosoma_padre_2):
    genes_padres = cromosoma_padre_1.genes + cromosoma_padre_2.genes
    genes_mutados = ""
    # genes_mutados = ''.join(random.choice(genes_padres) for i in range(TAMANIO_CADENA))
    for ubicacion in range(TAMANIO_CADENA):
        if (ubicacion in cromosoma_padre_1.genes_aptos):
            genes_mutados += cromosoma_padre_1.genes[ubicacion]
        elif (ubicacion in cromosoma_padre_2.genes_aptos):
            genes_mutados += cromosoma_padre_2.genes[ubicacion]
        else:
            genes_mutados +=  random.choice(genes_padres)
    cromosoma_hijo = Cromosoma(genes_mutados, TAMANIO_CADENA,cromosoma_padre_1.genes, cromosoma_padre_2.genes)
    return cromosoma_hijo

def algoritmo_genetico():
    cromosoma_ideal = None
    lista_poblacion = generar_lista_poblacion()
    lista_cromosomas_aptos = None
    lista_proxima_generacion = None
    while cromosoma_ideal == None:
        lista_cromosomas_aptos = devolver_cromosomas_aptos(lista_poblacion)  # 50% aptos
        lista_proxima_generacion = generar_proxima_generacion(lista_cromosomas_aptos, lista_poblacion)
        cromosoma_ideal = next((cromosoma for cromosoma in lista_proxima_generacion if cromosoma.genes == CADENA_OBJETIVO), None)
        lista_poblacion.clear()
        lista_poblacion = lista_proxima_generacion.copy()
        lista_cromosomas_aptos.clear()
        lista_proxima_generacion.clear()
    print(cromosoma_ideal.genes)

algoritmo_genetico()
