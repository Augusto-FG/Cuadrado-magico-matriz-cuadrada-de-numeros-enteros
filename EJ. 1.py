import random

def crear_matriz (n):
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz



def rellenar_matriz(matriz,n):
    filas = len(matriz)
    columnas = len(matriz)
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=random.randint(0,100)
    

def imprimir (matriz):
    filas = len (matriz)
    columnas = len (matriz[0])
    for f in range (filas):
        for c in range (columnas):
            print ("%3d" %matriz[f][c], end ="")
        print ()
        
        
def sumarcolumnas(mat):
    filas = len(mat)
    columnas = len(mat[0])
    sumacolumnas = [sum(mat[f][c] for f in range(filas)) for c in range(columnas)]
    return sumacolumnas
        
n = int (input("Ingrese tamaño matriz:"))

matriz = crear_matriz(n)

rellenar_matriz(matriz,n)

imprimir (matriz)