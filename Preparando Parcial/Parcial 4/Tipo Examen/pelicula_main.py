import pelicula
import random
import pickle
import os.path

def menu_de_opciones():
    print("\nMenu de Opciones")
    print("1-Mostrar")
    print("2-Buscar y cambiar importe")
    print("3-Generar archivo con especificaciones")
    print("4-Mostrar archivo punto 3")
    print("5-Buscar por número")
    print("6-Cantidad de películas de cada tipo por cada pais de origen")
    print("7-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op

def cargar_vector(v, n):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        num = random.randint(1, 100)
        tit = random.choice(abc)
        imp = round(random.uniform(1000, 30000000), 2)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)
        peli = pelicula.Pelicula(num, tit, imp, tipo, pais)
        add_in_order(v, peli)


def add_in_order(vector, registro):
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].titulo == registro.titulo:
            pos = c
            break

        if vector[c].titulo < registro.titulo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def mostrar_vector(peliculas):
    for peli in peliculas:
        print(pelicula.to_string(peli))

def buscar_titulo(peliculas, nom):
    izq = 0
    der = len(peliculas) - 1

    while izq <= der:
        c = (izq + der) // 2
        if peliculas[c].titulo == nom:
            return c
        if peliculas[c].titulo < nom:
            izq = c + 1
        else:
            der = c - 1
    return -1

def buscar_numero(peliculas, num):
    for i in range(len(peliculas)):
        if peliculas[i].numero == num:
            return i
    return -1

def generar_archivo(peliculas, x):
    m = open("peliculas.dat", "wb")
    for i in range(len(peliculas)):
        if peliculas[i].pais != 10 and peliculas[i].importe < x:
            pickle.dump(peliculas[i], m)
    m.close()

def mostrar_archivo():
    if not os.path.exists("peliculas.dat"):
        print("El archivo no existe...")
        return
    m = open("peliculas.dat", "rb")
    tam = os.path.getsize("peliculas.dat")
    while m.tell() < tam:
        peli = pickle.load(m)
        print(pelicula.to_string(peli))
    m.close()

def generar_matriz(peliculas):
    matriz = [[0] * 10 for f in range(20)]

    for i in range(len(peliculas)):
        fila = peliculas[i].pais
        columna = peliculas[i].tipo
        matriz[fila][columna] += 1

    return matriz

def mostrar_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                print("País:", i, "--- Tipo:", j, "--- Cantidad:", m[i][j])
        print()

def test():
    print("Películas de un Cine")
    n = int(input("Ingrese la cantidad de películas: "))
    peliculas = []
    cargar_vector(peliculas, n)
    op = -1

    while op != 7:
        op = menu_de_opciones()

        if op == 1:
            mostrar_vector(peliculas)

        elif op == 2:
            nom = input("Ingrese el título a buscar: ")
            pos = buscar_titulo(peliculas, nom)
            if pos == -1:
                print("Película no encontrada")
            else:
                print("Película encontrada...")
                imp = float(input("Ingrese el nuevo importe de la película: "))
                peliculas[pos].importe = imp
                print(pelicula.to_string(peliculas[pos]))
        elif op == 3:
            x = float(input("Ingrese el importe a comparar antes de grabar: "))
            generar_archivo(peliculas, x)

        elif op == 4:
            mostrar_archivo()

        elif op == 5:
            num = int(input("Ingrese el número a buscar: "))
            pos_num = buscar_numero(peliculas, num)
            if pos_num == -1:
                print("Película no encontrada")
            else:
                print("Película encontrada...")
                print(pelicula.to_string(peliculas[pos_num]))

        elif op == 6:
            matriz = generar_matriz(peliculas)
            mostrar_matriz(matriz)

        elif op == 7:
            print("Bye Bye")
        else:
            print("Opción no válida")


if __name__ == "__main__":
    test()
