"""
Turno 1 - Enunciado 1 (T1E1)

Un parque de diversiones, desea un programa para procesar los datos de los juegos que tiene disponible.
Por cada Juego se tienen los siguientes datos: código de identificación del juego, nombre del juego, el precio
de la entrada, la edad mínima para subir al juego y el sector donde se encuentra dentro del parque (un valor
entre 0 y 7 ambos incluidos, de la forma 0: Norte, 1: Noroeste, 2: Noreste, etc.). Se desea almacenar la información
referida a los n juegos en un arreglo de registros de tipo Juego (definir el tipo Juego y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
 que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de las n juegos. Valide que el tipo de juego sea un valor entre 0 y 7
 (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática
 (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de los juegos cuya edad mínima sea superior a un valor x, siendo x un valor que se
carga por teclado, en un listado ordenado de menor a mayor por código de identificación de juego.

3- Usando el arreglo creado en el punto 1, determine la cantidad de juegos disponibles en cada sector del parque.
 En total, 8 contadores usando un vector de conteo. Muestre sólo los resultados de los 5 primeros sectores.

4- De entre todas las edades mínimas del arreglo, determinar y mostrar la mayor. Luego muestre la cantidad de
juegos que tienen esa mayor edad mínima.

5- Determinar si existe un juego cuyo nombre sea igual a nom (que se carga por teclado) y su precio sea un valor
 entre a y b (siendo a y b valores que también se cargan por teclado). Si existe, mostrar sus datos. Si no existe,
  informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar
  sólo el primero que encuentre.
"""
import random
import juego


def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Cargar")
    print("2-Mostrar juegos de edad mínima x")
    print("3-Juegos por sector")
    print("4-Edad mínima mayor")
    print("5-Búsqueda de un juego determinado")
    print("6-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op


def validar_mayor_que(inf, mensaje="Ingrese un nro: ", flotante=False):
    if not flotante:
        valor = int(input(mensaje))
        while valor <= inf:
            print('¡Valor invalido!')

            valor = int(input(mensaje))
    else:
        valor = float(input(mensaje))
        while valor <= inf:
            print('¡Valor invalido!')

            valor = float(input(mensaje))
    return valor


def validar_rango(inf, sup, mensaje):
    valor = inf - 1
    while valor < inf or valor > sup:
        valor = int(input(mensaje))
        if valor < inf or valor > sup:
            print("Valor no válido...")
    return valor


def carga_manual(juegos):
    for i in range(len(juegos)):
        print("Juego", i+1)
        cod = validar_mayor_que(0, "Ingrese el código del juego: ")
        nombre = input("Ingrese el nombre del juego: ")
        precio = validar_mayor_que(0, "Ingrese el precio del juego: ", True)
        edad = validar_mayor_que(0, "Ingrese la edad mínima requerida para subir al juego: ")
        sector = validar_rango(0, 7, "Ingrese el sector del juego (0 a 7): ")

        juegos[i] = juego.Juego(cod, nombre, precio, edad, sector)


def carga_automatica(juegos):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(juegos)):
        cod = random.randint(1, 5000)
        nombre = "Juego " + random.choice(letras) + random.choice(letras) + random.choice(letras)
        precio = round(random.uniform(400, 1500), 2)
        edad = random.randint(3, 18)
        sector = random.randint(0, 7)

        juegos[i] = juego.Juego(cod, nombre, precio, edad, sector)


def codigo_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def mostrar_edadx(juegos, x):
    existen = False
    for i in range(len(juegos)):
        if juegos[i].edad > x:
            print(juego.to_string(juegos[i]))
            existen = True
    if not existen:
        print("No hay juegos con edad mayor a la ingresada...")


def contar_jsectores(juegos):
    c = [0] * 8
    for i in range(len(juegos)):
        c[juegos[i].sector] += 1

    return c


def mostrar_conteo(c):
    for i in range(5):
        print("Sector", i, ":", c[i])


def buscar_mayor_edad(v):
    mayor = v[0].edad
    for i in range(1, len(v)):
        if v[i].edad > mayor:
            mayor = v[i].edad
    return mayor


def contar_jedad(juegos, e):
    c = 0
    for i in range(len(juegos)):
        if juegos[i].edad == e:
            c += 1
    return c


def valor_entre(x, mn, mx):
    if mn < x < mx:
        return True
    return False


def search_juego(juegos, nom, a, b):
    for i in range(len(juegos)):
        if juegos[i].nombre == nom and valor_entre(juegos[i].precio, a, b):
            return i
    return -1


def test():
    print("Juegos de Parque de Diversiones")
    juegos = []

    op = -1
    carga = False

    while op != 6:
        print()
        op = menu_de_opciones()
        print()
        if op == 1:
            print("Carga")
            n = validar_mayor_que(0, "Ingrese la cantidad total de juegos a cargar: ")
            juegos = [None] * n
            tipo_c = validar_rango(0, 1, "Ingrese el tipo de carga(0:Manual, 1:Automática): ")
            print()
            if tipo_c == 0:
                carga_manual(juegos)
            else:
                carga_automatica(juegos)
            carga = True

        elif op == 2:
            if not carga:
                print("Debe realizar la carga del arreglo primero...Seleccione la opción 1")
            else:
                print("Juegos cuya edad mínima es mayor a x")
                x = int(input("Ingrese la edad x: "))
                codigo_sort(juegos)
                mostrar_edadx(juegos, x)

        elif op == 3:
            if not carga:
                print("Debe realizar la carga del arreglo primero...Seleccione la opción 1")
            else:
                print("Juegos por sector")
                contadores = contar_jsectores(juegos)
                mostrar_conteo(contadores)

        elif op == 4:
            if not carga:
                print("Debe realizar la carga del arreglo primero...Seleccione la opción 1")
            else:
                print("Edad mínima más grande requerida")
                mayor_edad = buscar_mayor_edad(juegos)
                c_juegos = contar_jedad(juegos, mayor_edad)
                print("La edad mínima mayor es:", mayor_edad)
                print("La cantidad de juegos con esta edad mínima es:", c_juegos)

        elif op == 5:
            if not carga:
                print("Debe realizar la carga del arreglo primero...Seleccione la opción 1")
            else:
                print("Búsqueda de un juego específico")
                nom = input("Ingrese el nombre del juego a buscar: ")
                a = float(input("Ingrese el precio mínimo del juego: "))
                b = float(input("Ingrese el precio máximo del juego: "))
                juego_buscado = search_juego(juegos, nom, a, b)
                print()
                if juego_buscado != -1:
                    print(juego.to_string(juegos[juego_buscado]))
                else:
                    print("No se ha encontrado el juego con estas especificaciones...")

        elif op == 6:
            print("Hasta la próxima...")
        else:
            print("Opción no válida...intente nuevamente")


if __name__ == "__main__":
    test()
