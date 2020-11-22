from constraint import *
from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "http://mapasenpdf.com/maps/educational/espana/previews/mapa-autonomc3adas.jpg")


# Problema 1
print("PROBLEMA 1")
problem = Problem()
"""
Variables:
0 1 2
3 4 5 
6 7 8
Dominio: {1, 2, 3}
"""
problem.addVariables(range(0, 9), range(1, 3 + 1))
problem.addConstraint(ExactSumConstraint(6), [0, 4, 8])
print("rowws -------")
for row in range(3):
    print(row)
    problem.addConstraint(AllDifferentConstraint(), [row * 3 + i for i in range(3)])
    problem.addConstraint(ExactSumConstraint(6), [row * 3 + i for i in range(3)])
    print([row * 3 + i for i in range(3)])
print("columnas -------")
for col in range(3):
    print(col)
    problem.addConstraint(AllDifferentConstraint(), [col * 3 + i for i in range(3)])
    problem.addConstraint(ExactSumConstraint(6), [col + 3 * i for i in range(3)])
    print([col + 3 * i for i in range(3)])

solutions1 = problem.getSolution()
print(solutions1)

# Problema 2
print("PROBLEMA 2")
""" 
Comentario
"""
problem2 = Problem()
variables = range(1,9)	
dominios = range(1,9)	
problem2.addVariables(variables, dominios)	# aniadir todass las variables

# cada reina tiene que estar en una columna separada
# conforme evoluciona el bucle se aniaden las restricciones
for columna1 in variables:
    for columna2 in variables:
        if columna1 < columna2:
            problem2.addConstraint(lambda row1, row2, columna1=columna1, columna2=columna2:
                abs(row1-row2) != abs(columna1-columna2) and	# revision diagonas
                row1 != row2, (columna1, columna2))				# revision horizontal

solution2 = problem2.getSolution()
print(solution2)

# Problema 3
print("PROBLEMA 3")
""" 
Al principio intente hacerlo con una matriz pero era imposible representar el mapa. Introduzco las variables y los dominios.
Variables: "GALICIA", "ASTURIAS", "CANTABRIA", "EUSKADI", "NAVARRA", "LA RIOJA", "ARAGON", "CATALONIA",
"CASTILLA LEON", "MADRID", "CASTILLA MANCHA", "VALENCIA", "BALEARES", "EXTREMADURA", "ANDALUCIA", "MURCIA", "CANARIAS"
Dominios: "rojo", "naranja", "verde"
He comprobado que con solo tres colores ya funciona.
"""
problem3 = Problem()
problem3.addVariables(["GALICIA", "ASTURIAS", "CANTABRIA", "EUSKADI", "NAVARRA", "LA RIOJA", "ARAGON", "CATALONIA",
"CASTILLA LEON", "MADRID", "CASTILLA MANCHA", "VALENCIA", "BALEARES", "EXTREMADURA", "ANDALUCIA", "MURCIA", "CANARIAS"], ["rojo", "naranja", "verde"])

problem3.addConstraint(AllDifferentConstraint(), ["GALICIA", "ASTURIAS", "CASTILLA LEON"]) 
problem3.addConstraint(AllDifferentConstraint(), ["CANTABRIA", "ASTURIAS", "CASTILLA LEON"]) 

problem3.addConstraint(AllDifferentConstraint(), ["EUSKADI", "CANTABRIA", "CASTILLA LEON"]) 
problem3.addConstraint(AllDifferentConstraint(), ["EUSKADI", "LA RIOJA", "CASTILLA LEON"]) 
problem3.addConstraint(AllDifferentConstraint(), ["EUSKADI", "LA RIOJA", "NAVARRA"]) 

problem3.addConstraint(AllDifferentConstraint(), ["LA RIOJA", "CASTILLA LEON", "ARAGON"]) 

problem3.addConstraint(AllDifferentConstraint(), ["NAVARRA", "LA RIOJA", "ARAGON"]) 

problem3.addConstraint(AllDifferentConstraint(), ["ARAGON", "CATALONIA", "NAVARRA"])
problem3.addConstraint(AllDifferentConstraint(), ["ARAGON", "CASTILLA LEON", "CASTILLA MANCHA"])
problem3.addConstraint(AllDifferentConstraint(), ["ARAGON", "CATALONIA", "VALENCIA"])
problem3.addConstraint(AllDifferentConstraint(), ["ARAGON", "CASTILLA MANCHA", "VALENCIA"])

problem3.addConstraint(AllDifferentConstraint(), ["CASTILLA MANCHA", "MURCIA", "VALENCIA"])
problem3.addConstraint(AllDifferentConstraint(), ["CASTILLA MANCHA", "MADRID", "CASTILLA LEON"])

problem3.addConstraint(AllDifferentConstraint(), ["EXTREMADURA", "CASTILLA MANCHA", "CASTILLA LEON"])
problem3.addConstraint(AllDifferentConstraint(), ["EXTREMADURA", "CASTILLA MANCHA", "ANDALUCIA"])

problem3.addConstraint(AllDifferentConstraint(), ["ANDALUCIA", "CASTILLA MANCHA", "MURCIA"])

solution3 = problem.getSolution()
print(solution3)


