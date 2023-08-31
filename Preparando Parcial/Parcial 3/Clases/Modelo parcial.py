"""
14. Modelo Parcial 2019
Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
Por cada trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o
nombre del mismo, el tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados),
el importe a cobrar por ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea
almacenar la información referida a los n trabajos en un arreglo de registros de trabajos (definir el Trabajo
 y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las
siguientes tareas:
los importes a cobrar.

1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del
 trabajo sea positivo y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual,
  o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas
   si lo desea. Pero al menos una debe programar.
2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes
 a cobrar.
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si
 hay varios trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de
  personal sea máxima).
4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado.
 Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida
  con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
5- Determinar y mostrar la cantidad de trabajos por tipo

"""
import random
import trabajo


def validar_mayor_que(inf):
    n = int(input("Valor (mayor a " + str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error...se pidió > " + str(inf) + " ...Cargue de nuevo: "))
    return n


def cargar_servicios(servicios):

    for i in range(len(servicios)):
        num = i + 1
        descripciones = ("limpieza profunda", "limpieza rápida", "acondicionamiento")
        desc = random.choice(descripciones)
        tipo = random.randint(0, 3)
        imp = random.random() * 10000 + 1
        cant = random.randint(1, 15)

        servicios[i] = trabajo.Trabajo(num, desc, tipo, imp, cant)


def mostrar_servicios(servicios):
    for i in range(len(servicios)):
        print(trabajo.to_string(servicios[i]))


def selection_sort(servicios):
    n = len(servicios)
    for i in range(n-1):
        for j in range(i + 1, n):
            if servicios[i].importe < servicios[j].importe:
                servicios[i], servicios[j] = servicios[j], servicios[i]


def mas_empleados(servicios):
    mayor = 0
    for i in range(1, len(servicios)):
        if servicios[i].cantidad > servicios[mayor].cantidad:
            mayor = i
    return mayor


def buscar_descripcion(servicios, d):
    for i in range(len(servicios)):
        if d == servicios[i].descripcion:
            return i
    return -1


def cantidad_por_tipo(servicios):
    cantidades = [0] * 4

    for i in range(len(servicios)):
        cantidades[servicios[i].tipo] += 1

    return cantidades


def mostrar_cantidades(cantidades, tipos):
    for i in range(len(cantidades)):
        print("Tipo: ", tipos[i], "--- Cantidad: ", cantidades[i])


def test():
    print("SERVICIOS DE LIMPIEZA")
    print("Ingrese la cantidad de servicios")
    n = validar_mayor_que(0)
    servicios = [None] * n

    op = -1
    charge = False
    while op != 6:
        print()
        print("Servicios - Menú de Opciones")
        print("Opción 1: Cargar")
        print("Opción 2: Ordenar y Mostrar")
        print("Opción 3: Trabajo con mayor personal afectado")
        print("Opción 4: Buscar por descripción")
        print("Opción 5: Cantidades por tipo de servicio")
        print("Opción 6: Salir")
        op = int(input("Ingrese su opción: "))

        if op == 1:
            cargar_servicios(servicios)
            charge = True

        elif op == 2:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                selection_sort(servicios)
                print()
                mostrar_servicios(servicios)

        elif op == 3:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                may = mas_empleados(servicios)
                print()
                print("El servicio con mayor cantidad de empleados:")
                print(trabajo.to_string(servicios[may]))

        elif op == 4:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                print()
                d = input("Ingrese la descripción a buscar: ")
                desc = buscar_descripcion(servicios, d)
                if desc == -1:
                    print("No se encontró tal registro...")
                else:
                    print("Registro encontrado")
                    print(trabajo.to_string(servicios[desc]))

        elif op == 5:
            if not charge:
                print("\nPrimero debe cargar el vector\n")
            else:
                print("Cantidad de Trabajos por tipo")
                cantidades = cantidad_por_tipo(servicios)
                tipos = ["interior", "exterior", "piletas", "tapizados"]
                mostrar_cantidades(cantidades, tipos)

        elif op == 6:
            print("Bye Bye")

        else:
            print("Valor no válido")


if __name__ == "__main__":
    test()
