"""
Torneo de Futbol
Desarrollar un programa para gestionar los puntos de un torneo de futbol.

Del torneo participan n equipos (n se ingresa por teclado). Por cada equipo, cargar 3 vectores paralelos con la siguiente información:

equipos: nombres de los mismos
puntos: total de puntos obtenidos en el torneo (máximo 20)
goles: total de goles anotados en el torneo
La carga debe implementarse tanto en forma manual como automática.

El programa debe luego mostrar las siguientes estadísticas

Tabla de Posiciones: ordenar el listado por orden descendente de puntaje y mostrarlo
Punteros: mostrar el o los equipos que tienen la mayor cantidad de puntos del torneo
Tabla de Descenso: Mostrar los últimos 5 equipos de la tabla de posiciones
Mejor desempeño: mostrar (en orden alfabético) los equipos que anotaron más de x goles en el torneo, siendo x un valor que se carga por teclado
Comparativo de goles: generar una tabla donde cada fila represente un equipo y cada columna una cantidad posible de puntos. La tabla debe contener la cantidad de goles realizados por el equipo. A partir de esa tabla, informar:
Total de goles para los equipos que tuvieron el máximo puntaje
Cantidad de equipos que no obtuvieron puntos ni marcaron goles
"""
import random


def validar(inf):
    n = int(input("Valor (mayor a " + str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error...se pidió > " + str(inf) + " ...Cargue de nuevo: "))
    return n


def validar_rango(inf, sup, mensaje):
    valor = inf - 1
    while valor < inf or valor > sup:
        valor = int(input(mensaje))
        if valor < inf or valor > sup:
            print("Valor no válido...")
    return valor


def carga_manual(e, p, g):
    for i in range(len(e)):
        e[i] = input("Nombre del equipo " + str(i+1) + ": ")
        p[i] = validar_rango(0, 20, "Puntos del equipo: ")
        print("Goles del equipo")
        g[i] = validar(-1)


def carga_automatica(e, p, g):
    team = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(e)):
        e[i] = random.choice(team) + random.choice(team) + random.choice(team) + " FC"
        p[i] = random.randint(0, 20)
        g[i] = random.randint(0, 50)


def carga(e, p, g):
    charge = -1
    while charge > 1 or charge < 0:
        charge = int(input("Carga manual(0) o automática(1): "))
        if charge == 0:
            carga_manual(e, p, g)
        elif charge == 1:
            carga_automatica(e, p, g)
        else:
            charge = int(input("Valor no válido...Carga manual(0) o automática(1): "))

def selection_sort(e, p, g):
    n = len(e)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if p[j] > p[i]:
                e[i], e[j] = e[j], e[i]
                p[i], p[j] = p[j], p[i]
                g[i], g[j] = g[j], g[i]

def tabla(e, p, g):
    for i in range(len(e)):
        r = ""
        r += "{:<7}".format(e[i])
        r += "{:^7}".format(str(p[i]))
        r += "{:<7}".format(str(g[i]))
        print(r)


def buscar_mayor(v):
    mayor = 0
    mayor2 = 0
    for i in range(1, len(v)):
        if v[i] > v[mayor]:
            mayor = i
        elif v[i] == v[mayor]:
            mayor2 = i

    return mayor, mayor2

def descenso(e):
    n = len(e)
    for i in range(n - 1, n - 6, -1):
        print(e[i])


def mejor_desempeno(e, g, x):
    n = len(e)
    for i in range(n):
        if g[i] > x:
            r = ""
            r += "{:<7}".format(e[i])
            r += "{:<7}".format(str(g[i]))
            print(r)

def test():
    print("Torneo de Futbol")
    print("Ingrese la cantidad de equipos participantes")
    n = validar(0)
    equipos = [""] * n
    puntos = [0] * n
    goles = [0] * n

    carga(equipos, puntos, goles)
    selection_sort(equipos, puntos, goles)
    print("Tabla de Posiciones:")
    tabla(equipos, puntos, goles)

    puntero, segundo = buscar_mayor(puntos)
    if puntos[puntero] == puntos[segundo] and equipos[puntero] != equipos[segundo]:
        print("Punteros: ", equipos[puntero], equipos[segundo])
    else:
        print("Puntero: ", equipos[puntero])

    print()
    print("Equipos en descenso:")
    descenso(equipos)

    print()
    print("Mejor desempeño")
    print("Ingrese la cantidad de goles que los equipos debieron superar")
    x = validar(0)
    print()
    mejor_desempeno(equipos, goles, x)


    print()






if __name__ == "__main__":
    test()
