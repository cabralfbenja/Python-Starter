"""
Enunciado:
Los organizadores de una competencia artística desean un programa para procesar los datos de los participantes
inscriptos.
Para cada participante se tienen los siguientes datos: código alfanumérico de identificación del participante
(deberá estar conformado por el prefijo "ar", un guion bajo, y un número entero múltiplo de 3), apellido del
participante, la localidad de origen del participante ( valor entero entre 0 y 9, por ejemplo: 0: Rio Primero,
1: Río Cuarto, etc.), tipo de disciplina (valor numérico entre 0 y 4, por ejemplo: 0: dibujo, 1: pintura,
2: teatro, etc.) y el puntaje obtenido para ese participante (valor entre 1 y 10; si es 0, indica que el
participante no se presentó a la prueba).
Se desea almacenar información referida a los n participantes inscriptos en la competencia en un arreglo de
registros de tipo Participante (definir el tipo Participante y cargar n por teclado).
Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las
siguientes tareas:
1. Cargar el arreglo pedido con los datos de los n participantes. Valide que la localidad origen del participante
sea mayor o igual a cero y menor o igual que 9.  Valide que el tipo de disciplina sea mayor o igual a cero y menor
o igual que 4. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios) o puede disponer de ambas técnicas si lo. Pero al menos una debe programar.
2. Mostrar todos los datos de todos los participantes.
3. Determinar y mostrar la cantidad de participantes por cada tipo de localidad de origen posible y por cada tipo
de disciplina en la que haya participado. En total, 10 * 5 contadores usando una matriz de conteo. Mostrar sólo
los valores de la matriz que sean distintos de cero.
4. Determinar y mostrar el puntaje total obtenido por los participantes por cada tipo de localidad de origen
posible y por cada tipo de competencia en la que haya participado. En total, 10 * 5 acumuladores usando una
matriz de acumulación. Mostrar sólo los valores de la matriz que sean distintos de cero.
5.  Calcular y mostrar el puntaje obtenido por los participantes por cada tipo de localidad de origen posible y
por cada tipo de disciplina en la que haya participado. En total, 10 * 5  valores promedios. Para generar y mostrar
esta información, deberá haber generado las matrices de los puntos 3 y 4.  En caso contrario, informar que antes
debe haber seleccionado las opciones correspondientes a dichas consignas.

"""

import random
import participante


def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Cargar")
    print("2-Mostrar")
    print("3-Cantidad de participantes por localidad y disciplina")
    print("4-Puntaje total obtenido por localidad y disciplina")
    print("5-Puntaje promedio por localidad y disciplina")
    print("6-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def carga(participantes):
    n = len(participantes)
    letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(n):
        cod = "ar-" + str(3 * random.randint(0, 1000))
        apellido = random.choice(letra1) + random.choice(letra2)
        loc = random.randint(0, 9)
        disc = random.randint(0, 4)
        puntaje = random.randint(0, 10)

        participantes[i] = participante.Participante(cod, apellido, loc, disc, puntaje)
        print()


def mostrar_todo(participantes):
    for p in participantes:
        print(participante.to_string(p))


def contar(participantes):
    c = [[0] * 10 for f in range(5)]
    for i in range(len(participantes)):
        disc = participantes[i].disciplina
        loc = participantes[i].localidad
        c[disc][loc] += 1
    return c


def mostrar_matriz(c, mensaje):
    n = len(c)
    m = len(c[0])
    for i in range(n):
        for j in range(m):
            if c[i][j] != 0:
                print("Disciplina:", i, "--- Localidad:", j, mensaje, c[i][j])


def contar_puntos(participantes):
    c = [[0] * 10 for f in range(5)]
    for i in range(len(participantes)):
        disc = participantes[i].disciplina
        loc = participantes[i].localidad
        c[disc][loc] += participantes[i].puntaje
    return c


def avg(puntajes, cantidades):
    n = len(puntajes)
    m = len(puntajes[0])
    promedios = [[0] * 10 for f in range(5)]
    for i in range(n):
        for j in range(m):
            if cantidades[i][j] != 0:
                promedios[i][j] = round(puntajes[i][j] / cantidades[i][j], 2)
    return promedios


def test():
    print("Participantes de una Competencia Artística")
    op = -1
    participantes = []
    cantidades = [[0] * 10 for f in range(5)]
    puntajes = [[0] * 10 for f in range(5)]
    charge = False
    op3 = False
    op4 = False

    while op != 6:
        print()
        op = menu_de_opciones()

        if op == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad total de participantes: ")
            participantes = [0] * n
            carga(participantes)
            charge = True

        elif op == 2:
            if not charge:
                print("Primero realice la carga...")
            else:
                print("-" * 40, "PARTICIPANTES", "-" * 40)
                mostrar_todo(participantes)

        elif op == 3:
            if not charge:
                print("Primero realice la carga...")
            else:
                print("-" * 30, "PARTICIPANTES POR DISCIPLINA Y LOCALIDAD", "-" * 30)
                cantidades = contar(participantes)
                mostrar_matriz(cantidades, "--- Cantidad:")
                op3 = True

        elif op == 4:
            if not charge:
                print("Primero realice la carga...")
            else:
                print("-" * 30, "PUNTAJES POR DISCIPLINA Y LOCALIDAD", "-" * 30)
                puntajes = contar_puntos(participantes)
                mostrar_matriz(puntajes, "--- Puntaje:")
                op4 = True

        elif op == 5:
            if not charge:
                print("Primero realice la carga...")
            elif not op3 or not op4:
                print("Debe realizar las opciones 3 y 4 antes de la 5")
            else:
                promedios = avg(puntajes, cantidades)
                mostrar_matriz(promedios, "--- Promedio:")

        elif op == 6:
            print("Bye Bye")

        else:
            print("Opción no válida...")

if __name__ == "__main__":
    test()
