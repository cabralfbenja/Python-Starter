# 1. Tren de la Costa
# Desarrollar un programa que represente el recorrido de ida y vuelta del Tren de la Costa.
# El recorrido del tren abarca las siguientes estaciones: Maipú, Borges, Libertador, Anchorena, Barrancas,
# San Isidro R, Punta Chica, Marina Nueva, San Fernando R, Canal, Delta.
# Se pide cargar un vector que contenga el nombre de las estaciones y otros dos que representen el viaje de ida y de
# vuelta del tren, respectivamente. En los dos últimos, se cargará la cantidad de pasajeros que ascendieron al
# tren en la estación correspondiente.
# Con la información cargada, plantear el siguiente menú de opciones:
# 1) Mostrar los datos cargados
# 2) Cuántos pasajeros en total subieron en el viaje de ida, y cuántos en el viaje de vuelta
# 3) En qué estación subió la mayor cantidad de pasajeros, durante el viaje de ida
# 4) En cuántas estaciones del viaje de vuelta no subieron pasajeros, y qué porcentaje representan sobre el total de estaciones
# 4) Mostrar las estaciones la cantidad de pasajeros del viaje de ida fue mayor a la del viaje de vuelta.
import random


def carga(ida, vuelta):
    for i in range(len(ida)):
        ida[i] = random.randint(0, 100)
        vuelta[i] = random.randint(0, 100)


def mostrar_vector(estaciones, ida, vuelta):
    for i in range(len(estaciones)):
        print("Estación:", estaciones[i], "-Cantidad de pasajeros ida:", ida[i], "-Cantidad de pasajeros vuelta:",
              vuelta[i])


def acumular_vector(v):
    total = 0
    for i in range(len(v)):
        total += v[i]
    return total

def buscar_mayor(v):
    mayor = 0
    for i in range(1, len(v)):
        if v[i] > v[mayor]:
            mayor = i
    return mayor


def estacion_sp(v):
    sin_pasajeros = 0
    for i in range(len(v)):
        if v[i] == 0:
            sin_pasajeros += 1
    return sin_pasajeros


def porcentaje(subtotal, total):
    pct = (subtotal / total) * 100

    return round(pct, 2)


def comparar(estaciones, ida, vuelta):
    print("Estaciones con más pasajeros de ida que vuelta")
    hay = False
    for i in range(len(estaciones)):
        if ida[i] > vuelta[i]:
            print("Estación: ", estaciones[i])
            hay = True
    if not hay:
        print("No hay estaciones con más pasajeros de ida que vuelta")

def principal():
    ida = [0] * 11
    vuelta = [0] * 11
    estaciones = ["Maipú", "Borges", "Libertador", "Anchorena", "Barrancas", "San Isidro R", "Punta Chica", "Marina Nueva", "San Fernando R", "Canal", "Delta"]

    op = 1
    charge = False
    while op != 7:
        print("Tren de la Costa - Menú de Opciones")
        print("Opción 1: Cargar")
        print("Opción 2: Mostrar")
        print("Opción 3: Total en ida y en vuelta")
        print("Opción 4: Mostrar estación con mayor ingreso de pasajeros en la ida")
        print("Opción 5: Cantidad de estaciones sin pasajeros y el porcentaje que representan")
        print("Opción 6: Mostrar las estaciones donde la cantidad de pasajeros de ida fue mayor a la de vuelta")
        print("Opción 7: Salir")
        op = int(input("Ingrese su opción: "))

        if op == 1:
            carga(ida, vuelta)
            charge = True
        elif op == 2:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                mostrar_vector(estaciones, ida, vuelta)
        elif op == 3:
            print("Total ida: ", acumular_vector(ida), "- Total vuelta: ", acumular_vector(vuelta))
        elif op == 4:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                pos_mayor = buscar_mayor(ida)
                print("La estación con mayor cantidad de pasajeros en la ida: ", estaciones[pos_mayor])
        elif op == 5:
            no_pasajeros = estacion_sp(vuelta)
            print("Cantidad de estaciones donde no subieron pasajeros en la vuelta:", no_pasajeros)
            print("Porcentaje sobre el total: ", porcentaje(no_pasajeros, len(estaciones)))

        elif op == 6:
            comparar(estaciones, ida, vuelta)
        elif op == 7:
            print("Bye Bye")
        else:
            print("Opción Incorrecta!")


if __name__ == "__main__":
    principal()
