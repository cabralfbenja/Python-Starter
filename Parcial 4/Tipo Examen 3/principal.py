"""
Una compañía de servicios nos pide un sistema para los consumos de sus clientes.  De cada consumo se conoce un número
de identificación, el nombre del cliente,  el mes (valor de 1 a 12), el tipo de cliente (0: residencial,  1: industrial,
2: comercial) y el monto.
Se pide:
1) Generar un archivo binario de consumos. Mostrar el archivo.
2) A partir del archivo generar un vector con todos los consumos. El vector debe generarse ordenado por dni del cliente.
3) Mostrar el vector a razón de una línea por registro.
4) Buscar un gasto con número num, siendo num un valor que se ingresa por teclado. Si existe mostrar sus datos. Si no
existe mostrar un mensaje de error.
5) Generar una matriz de acumulación de monto por mes y por tipo de cliente.
6) Buscar un gasto con dni d, siendo d un valor que se ingresa por teclado. Si existe mostrar sus datos. Si no existe
mostrar un mensaje de error.
"""
from registro import *
import random
import pickle
import os


def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Generar y mostrar archivo")
    print("2-Generar vector a partir del archivo")
    print("3-Mostrar vector")
    print("4-Buscar gasto por número")
    print("5-Generar matriz de montos acumulados por tipo y mes")
    print("6-Buscar gasto por nombre")
    print("7-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op


def generar_archivo():
    n = random.randint(10, 100)
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m = open("consumos.dat", "wb")
    for i in range(n):
        num = i + 1
        cli = random.choice(abecedario) + random.choice(abecedario) + random.choice(abecedario)
        mes = random.randint(1, 12)
        tipo = random.randint(0, 2)
        monto = round(random.uniform(500, 5000), 2)
        registro = Consumo(num, cli, mes, tipo, monto)
        pickle.dump(registro, m)
        m.flush()
    m.close()
    print("Archivo generado...")


def mostrar_archivo():
    FD = "consumos.dat"
    if not os.path.exists(FD):
        print("Error...el archivo no existe")
        return
    m = open(FD, "rb")
    size = os.path.getsize(FD)
    while m.tell() < size:
        registro = pickle.load(m)
        print(to_string(registro))
    m.close()


def add_in_order(vector, registro):
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].cliente == registro.cliente:
            pos = c
            break

        if vector[c].cliente < registro.cliente:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def generar_vector():
    vector = []
    if not os.path.exists("consumos.dat"):
        print("Error...el archivo no existe")
        return
    m = open("consumos.dat", "rb")
    size = os.path.getsize("consumos.dat")
    while m.tell() < size:
        reg = pickle.load(m)
        add_in_order(vector, reg)
    m.close()

    return vector


def mostrar_vector(vector):
    for v in vector:
        print(to_string(v))


def busqueda_secuencial(v, num):
    for i in range(len(v)):
        if v[i].numero == num:
            return i
    return -1


def generar_matriz(v):
    mat = [[0] * 12 for f in range(3)]
    for i in range(len(v)):
        fila = v[i].tipo
        col = v[i].mes - 1
        mat[fila][col] += v[i].monto
    return mat


def mostar_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                print("Tipo:", i, "--- Mes:", j + 1, "--- Monto Acumulado:", round(m[i][j], 2))
        print()

def busqueda_binaria(v, nom):
    izq = 0
    der = len(v) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].cliente == nom:
            return c
        if v[c].cliente < nom:
            izq = c + 1
        else:
            der = c - 1
    return -1


def test():
    print("COMPAÑÍA DE SERVICIOS")
    op = -1
    vector = False
    consumos = []

    while op != 7:
        print()
        op = menu_de_opciones()
        print()

        if op == 1:
            generar_archivo()
            mostrar_archivo()
        elif op == 2:
            consumos = generar_vector()
            vector = True
            print("Vector generado...")
        elif op == 3:
            if vector:
                print("-" * 50, "Consumos", "-" * 50)
                mostrar_vector(consumos)
            else:
                print("El vector no ha sido generado...")
        elif op == 4:
            if vector:
                print("Búsqueda por número")
                num = int(input("Ingrese el número de gasto a buscar: "))
                pos = busqueda_secuencial(consumos, num)
                if pos != -1:
                    print("Gasto encontrado...")
                    print(to_string(consumos[pos]))
                else:
                    print("Gasto no encontrado")
            else:
                print("El vector no ha sido generado...")

        elif op == 5:
            if vector:
                mat = generar_matriz(consumos)
                mostar_matriz(mat)

            else:
                print("El vector no ha sido generado...")

        elif op == 6:
            if vector:
                print("Búsqueda por nombre")
                nom = input("Ingrese el nombre de la persona a buscar: ")
                pos = busqueda_binaria(consumos, nom)
                if pos != -1:
                    print("Gasto encontrado...")
                    print(to_string(consumos[pos]))
                else:
                    print("Gasto no encontrado")

            else:
                print("El vector no ha sido generado...")

        elif op == 7:
            print("Bye Bye")
        else:
            print("Valor no válido...")


if __name__ == "__main__":
    test()
