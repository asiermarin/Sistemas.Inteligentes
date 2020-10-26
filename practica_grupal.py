from collections import deque
import math 

mat = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]
q1 = []
anchura = 0
altura = 0
for i in mat:
    anchura = 0
    for j in i:
        if j > 0:
            q1.append([anchura,altura])
        anchura = anchura+1
    altura = altura+1
q2 = q1
q1 = []
while q2 != []:
    primer_valor = q2[0]
    if primer_valor[0]-1 >= 0:
        if mat[primer_valor[0]-1][primer_valor[1]]<0:
            mat[primer_valor[0]-1][primer_valor[1]] = abs(mat[primer_valor[0]-1][primer_valor[1]])
            q1.append([primer_valor[0]-1, primer_valor[1]])
    if primer_valor[0]+1 < len(mat):
        if mat[primer_valor[0]+1][primer_valor[1]]<0:
            mat[primer_valor[0]+1][primer_valor[1]] = abs(mat[primer_valor[0]+1][primer_valor[1]])
            q1.append([primer_valor[0]+1, primer_valor[1]])
    if primer_valor[1]-1 >= 0:
        if mat[primer_valor[0]][primer_valor[1]-1]<0:
            mat[primer_valor[0]][primer_valor[1]-1] = abs(mat[primer_valor[0]][primer_valor[1]-1])
            q1.append([primer_valor[0], primer_valor[1]-1])
    if primer_valor[1]+1 < len(mat):
        if mat[primer_valor[0]][primer_valor[1]+1]<0:
            mat[primer_valor[0]][primer_valor[1]+1] = abs(mat[primer_valor[0]][primer_valor[1]+1])
            q1.append([primer_valor[0], primer_valor[1]+1])
if q1 == []:
    print(pasos)
    pasos= pasos - 1
pasos = pasos + 1
                        
    