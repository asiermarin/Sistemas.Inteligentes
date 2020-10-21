from collections import deque
import math 

mat = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]
q1 = []
x = 0
y = 0
for i in mat:
    x = 0
    for j in i:
        if j > 0:
            q1.append([x,y])
        x = x+1
    y = y+1
q2 = q1
q1 = []
while q2 != []:
    base = q2[0]
    if base[0]-1 >= 0:
        if mat[base[0]-1][base[1]]<0:
            mat[base[0]-1][base[1]] = abs(mat[base[0]-1][base[1]])
            q1.append([base[0]-1, base[1]])
    if base[0]+1 < len(mat):
        if mat[base[0]+1][base[1]]<0:
            mat[base[0]+1][base[1]] = abs(mat[base[0]+1][base[1]])
            q1.append([base[0]+1, base[1]])
    if base[1]-1 >= 0:
        if mat[base[0]][base[1]-1]<0:
            mat[base[0]][base[1]-1] = abs(mat[base[0]][base[1]-1])
            q1.append([base[0], base[1]-1])
    if base[1]+1 < len(mat):
        if mat[base[0]][base[1]+1]<0:
            mat[base[0]][base[1]+1] = abs(mat[base[0]][base[1]+1])
            q1.append([base[0], base[1]+1])
for i in mat:
    print(i)
if q1 == []:
    print(pasos)
    pasos= pasos - 1
pasos = pasos + 1
                        
    