import random

OBJETOS_POSIBLES = [['Hacha', 32252, 68674],

['Moneda de bronce', 225790, 471010],

['Corona', 468164, 944620],

['Estatua de diamante', 489494, 962094],

['Cinturón de esmeralda belt', 35384, 78344],

['Fósil', 265590, 579152],

['Moneda de oro', 497911, 902698],

['Casco', 800493, 1686515],

['Tinta', 823576, 1688691],

['Cofre de joyas', 552202, 1056157],

['Cuchillo', 323618, 677562],

['Espada', 382846, 833132],

['Máscara', 44676, 99192],

['Collar', 169738, 376418],

['Insignia', 610876, 1253986],

['Perlas', 854190, 1853562],

['Carcaj', 671123, 1320297],

['Anillo de rubí', 698180, 1301637],

['Pulsera de plata', 446517, 859835],

['Reloj', 909620, 1677534],

['Uniforme', 904818, 1910501],

['Veneno', 730061, 1528646],

['Bufanda de lana', 931932, 1827477],

['Arco', 952360, 2068204],

['Libro', 926023, 1746556],

['Copa de zinc', 978724, 2100851]]

PESO_MAXIMO = 6404180
POSICION_NOMBRE_OBJETO = 0
POSICION_PESO_OBJETO = 1
POSICION_VALOR_OBJETO = 2

POBALCION = 100
PORCENTAJE_POBLACION_HIJOS = 0.9
PORCENTAJE_APTOS_NECESARIA_INICIAL = 0.5
PORCENTAJE_MAS_APTOS = 0.2

PESO_MEDIO = None
VALOR_MEDIO = None

CONVERSION_APTITUD = 0

def calcular_media_peso():
    global PESO_MEDIO
    peso_total = 0
    for objeto in OBJETOS_POSIBLES:
         peso_total = peso_total + objeto[POSICION_PESO_OBJETO]
    PESO_MEDIO = peso_total / 25

def calcular_media_valor():
    global VALOR_MEDIO
    valor_total = 0
    for objeto in OBJETOS_POSIBLES:
         valor_total = valor_total + objeto[POSICION_VALOR_OBJETO]
    VALOR_MEDIO = valor_total / 25

class Objeto:
    
    def __init__(self, nombre, peso, valor, objeto_padre_1, objeto_padre_2):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
        self.aptitud = 0
        if (objeto_padre_1 != None):
            self.nombre_padre_1 = objeto_padre_1.nombre
            self.nombre_padre_2 = objeto_padre_2.nombre
        else:
            self.nombre_padre_1 = None
            self.nombre_padre_2 = None
        # self.determinar_aptitud()
        self.determinar_aptitud_avanzada()

    def determinar_aptitud(self):
        self.aptitud = self.valor / self.peso # cuanto mayor sea la aptitud, mas vale respecto a peso
        print(f"Objeto: {self.nombre}:{self.peso}, {self.valor}  ------>  Aptitud: {self.aptitud} --- Objetos padres:{self.nombre_padre_1, self.nombre_padre_1}")
    
    def determinar_aptitud_avanzada(self):
        global PESO_MEDIO
        global VALOR_MEDIO
        global CONVERSION_APTITUD
        if (self.peso < PESO_MEDIO):
            self.aptitud = self.aptitud + ((PESO_MEDIO - self.peso) * CONVERSION_APTITUD)
        if (self.valor > VALOR_MEDIO):
            self.aptitud = self.aptitud + (self.valor - VALOR_MEDIO) 
        print(f"Objeto: {self.nombre}:{self.peso}, {self.valor}  ------>  Aptitud: {self.aptitud} --- Objetos padres:{self.nombre_padre_1, self.nombre_padre_1}")

def generar_lista_poblacion():
    print("Generando lista")
    poblacion = []
    for i in range(POBALCION):
        objeto = random.choice(OBJETOS_POSIBLES)
        nuevo_objeto = Objeto(objeto[POSICION_NOMBRE_OBJETO], objeto[POSICION_PESO_OBJETO], objeto[POSICION_VALOR_OBJETO], None, None)
        poblacion.append(nuevo_objeto)
    return poblacion

# Devolvemos los 50 mejores
def devolver_cromosomas_aptos(lista_poblacion):
    print("Devolviendo cromosomas aptos")
    lista_poblacion.sort(key=lambda x: x.aptitud, reverse=True)
    numero_lista_aptos_necesaria = devolver_numero_necesario_segun_porcentaje(lista_poblacion, PORCENTAJE_APTOS_NECESARIA_INICIAL) # 50
    lista_aptos = lista_poblacion[:numero_lista_aptos_necesaria]
    return lista_aptos

def devolver_numero_necesario_segun_porcentaje(lista, porcentaje):
    numero_poblacion = len(lista)
    nuemro_necesario = int(numero_poblacion * porcentaje)
    return nuemro_necesario

def generar_proxima_generacion(lista_objetos_aptos, lista_poblacion):
    print("Generando proxima generacion")
    rango_mas_aptos = devolver_numero_necesario_segun_porcentaje(lista_objetos_aptos, PORCENTAJE_MAS_APTOS) # 10
    rango_lista_hijos = devolver_numero_necesario_segun_porcentaje(lista_poblacion, PORCENTAJE_POBLACION_HIJOS) # 90
    lista_proxima_generacion = lista_objetos_aptos[:rango_mas_aptos] # ya tenemos el 10%
    lista_hijos = reproducir_hijos(lista_objetos_aptos, rango_lista_hijos) # Otro 90%
    lista_proxima_generacion.extend(lista_hijos)
    lista_proxima_generacion.sort(key=lambda x: x.aptitud, reverse=True)
    return lista_proxima_generacion

def reproducir_hijos(lista_objetos_aptos, rango_lista_hijos):
    lista_hijos = []
    for i in range(rango_lista_hijos):
        objeto_padre_1 = lista_objetos_aptos[random.randrange(len(lista_objetos_aptos))]
        objeto_padre_2 = lista_objetos_aptos[random.randrange(len(lista_objetos_aptos))]
        lista_hijos.append(mutacion(objeto_padre_1, objeto_padre_2))
    return lista_hijos

def mutacion(objeto_padre_1, objeto_padre_2):
    objeto_hijo = None
    if (objeto_padre_1.aptitud > objeto_padre_2.aptitud):
        objeto_hijo = Objeto(
            nombre = objeto_padre_1.nombre, 
            peso = objeto_padre_1.peso, 
            valor = objeto_padre_1.valor, 
            objeto_padre_1 = objeto_padre_1, 
            objeto_padre_2 = objeto_padre_2)
    else:
        objeto_hijo = Objeto(
            nombre = objeto_padre_2.nombre, 
            peso = objeto_padre_2.peso, 
            valor = objeto_padre_2.valor, 
            objeto_padre_1 = objeto_padre_1, 
            objeto_padre_2 = objeto_padre_2)
    return objeto_hijo

def calcular_peso_total_nueva_generacion(lista_poblacion):
    peso_total = 0
    for objeto in lista_poblacion:
         peso_total = peso_total + objeto.peso
    return peso_total

def calcular_conversion_aptitud():
    global PESO_MEDIO
    global VALOR_MEDIO
    global CONVERSION_APTITUD
    CONVERSION_APTITUD = VALOR_MEDIO / PESO_MEDIO

def algoritmo_genetico():
    global PESO_MAXIMO
    global PESO_MEDIO
    global VALOR_MEDIO
    peso_total = 100000000000
    pasos = 0
    calcular_media_peso()
    calcular_media_valor()
    calcular_conversion_aptitud()
    lista_poblacion = generar_lista_poblacion()
    lista_objetos_aptos = None
    lista_proxima_generacion = None
    while peso_total > PESO_MAXIMO or pasos < 20:
        # PESO_MEDIO = PESO_MEDIO - 10000
        # VALOR_MEDIO = VALOR_MEDIO + 50000
        lista_objetos_aptos = devolver_cromosomas_aptos(lista_poblacion)  # 50% aptos
        lista_proxima_generacion = generar_proxima_generacion(lista_objetos_aptos, lista_poblacion)
        lista_poblacion.clear()
        lista_poblacion = lista_proxima_generacion.copy()
        peso_total = calcular_peso_total_nueva_generacion(lista_poblacion)
        lista_objetos_aptos.clear()
        lista_proxima_generacion.clear()
        pasos = pasos + 1

algoritmo_genetico()