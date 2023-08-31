"""
1. Elecciones
Luego de las elecciones nacionales, la junta electoral debe procesar 2 archivos con el fin de obtener los datos
 del ganador de la elecciones. El primer archivo se llama votos.dat y contiene un listado con Votos, cada voto
 contiene los siguientes datos: candidato (codificado de 0 a 6), provincia (codificada de 0 a 20) y votante. Y
 el segundo archivo candidatos.dat que contiene un listado con Candidatos, cada candidato contiene código y nombre.

Se pide:

Mostrar el listado completo del archivo de votos.

Generar una matriz en donde cada fila es una provincia y cada columna un candidato; y en sus componentes este
la cantidad de votos que recibió ese candidato en esa provincia.

Mostrar con la matriz el nombre del candidato que ganó las elecciones, junto con la cantidad de votos obtenida.
"""
from voto import *
import pickle
import os.path

def mostrar():
    m = open("votos.dat", "rb")
    size = os.path.getsize("votos.dat")

    while m.tell() < size:
        votante = pickle.load(m)
        print(to_string(votante))
    m.close()

def generar_matriz():
    matriz = [[0] * 7 for f in range(21)]
    votos = [0] * 7
    m = open("votos.dat", "rb")
    size = os.path.getsize("votos.dat")

    while m.tell() < size:
        v = pickle.load(m)
        fila = v.provincia
        columna = v.candidato
        matriz[fila][columna] += 1
        votos[columna] += 1
    m.close()
    return matriz, votos


def mostrar_matriz(c, mensaje):
    n = len(c)
    m = len(c[0])
    for i in range(n):
        for j in range(m):
            if c[i][j] != 0:
                print("Provincia:", i, "--- Candidato:", j, mensaje, c[i][j])
        print()


def buscar_mayor(v):
    mayor = 0
    for i in range(1, len(v)):
        if v[i] > v[mayor]:
            mayor = i
    return mayor


def buscar_nombre(ganador):
    m = open("candidatos.dat", "rb")
    size = os.path.getsize("candidatos.dat")

    while m.tell() < size:
        candidato = pickle.load(m)
        if candidato.codigo == ganador:
            nombre = candidato.nombre
    m.close()
    return nombre


def test():
    print("Votos:")
    mostrar()
    matriz, votos = generar_matriz()
    print("\nVotos de cada candidato por provincia:")
    mostrar_matriz(matriz, "--- Votos:")
    ganador = buscar_mayor(votos)

    nombre_g = buscar_nombre(ganador)

    print("El candidato ganador fue: " + nombre_g + " --- Votos:", votos[ganador])

if __name__ == "__main__":
    test()
