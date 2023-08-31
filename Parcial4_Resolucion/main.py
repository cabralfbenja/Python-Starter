"""
Una empresa que distribuye artículos a diferentes puntos del país necesita mantener información sobre los distintos
envíos que realiza. Por cada envío se registran los siguientes datos: número de identificación (un entero),
descripción del envío (una cadena), monto del envío, provincia destino (un valor entre 0 y 23 incluidos, por
ejemplo: 0: Córdoba, 1: San Luis, etc.), tipo de artículo enviado (un número entero entre 0 y 29 incluidos,
para indicar (por ejemplo): 0: silla, 1: computadora, etc.) y el barrio de entrega (una cadena). Se pide definir
un tipo registro Envio con los campos que se indicaron, y un programa completo con menú de opciones para hacer
lo siguiente:

1- Cargar los datos de n registros de tipo Envío en un arreglo de registros (cargue n por teclado). El arreglo
debe crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los envíos,
y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente
incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de
inserción ordenada pero con búsqueda secuencial. Puede cargar los datos manualmente, o puede generarlos
aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe
ser automática). Valide que la provincia destino y el tipo de artículo estén dentro de los valores descriptos y
recuerde que estos son números enteros.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea, pero muestre solo los datos de los
registros cuyo tipo sea mayor al valor k que se carga por teclado.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual a num
(cargar num por teclado). Si existe, mostrar por pantalla todos sus datos. Si no existe, informar con un mensaje.
La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

4- Guarde en un archivo los registros del arreglo cuyo tipo de articulo vendido sea 2 o 5 y cuyo monto del
envío este comprendido entre dos valores x e y (ambos incluidos) que se ingresan por teclado.

5- Muestre el archivo que creó en el punto 4, a razón de un registro por línea en la pantalla y al final mostrar
una línea adicional que informe el promedio de los montos de los envíos que se mostraron.
"""
from registro import *
import random
import pickle
import os.path


def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Cargar arreglo de envíos")
    print("2-Mostrar envíos cuyo tipo sea mayor a k")
    print("3-Búsqueda por id")
    print("4-Crear Archivo con especificaciones")
    print("5-Mostrar Archivo")
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


def generar_sin_repetir(m):
    a = 1
    while a == 1:
        a = 0
        num = random.randint(0, 99999)
        for i in range(len(m)):
            if a == m[i]:
                a = 1

    return num


def add_in_order(vector, registro):
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].id == registro.id:
            pos = c
            break

        if vector[c].id < registro.id:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def cargar_arreglo(v, n):
    descripciones = ("Extenso", "Sencillo", "Complicado", "Simple")
    barrios = ("Urca", "Cerro de las Rosas", "Barrio Jardín", "Chateau", "Villa Belgrano", "Nueva Córdoba")
    nums = []
    for i in range(n):
        num = generar_sin_repetir(nums)
        desc = random.choice(descripciones)
        monto = round(random.uniform(500, 4000), 2)
        prov = random.randint(0, 23)
        tipo = random.randint(0, 29)
        barrio = random.choice(barrios)
        envio = Envio(num, desc, monto, prov, tipo, barrio)
        add_in_order(v, envio)
    return v


def mostrar_arreglo(v, k):
    n = len(v)
    for i in range(n):
        if v[i].tipo > k:
            print(to_string(v[i]))


def busqueda_binaria(envios, num):
    izq = 0
    der = len(envios) - 1

    while izq <= der:
        c = (izq + der) // 2
        if envios[c].id == num:
            return c
        if envios[c].id < num:
            izq = c + 1
        else:
            der = c - 1
    return -1


def crear_archivo(v, x, y):
    m = open("envios.dat", "wb")
    for i in range(len(v)):
        if (v[i].tipo == 2 or v[i].tipo == 5) and x <= v[i].monto <= y:
            pickle.dump(v[i], m)
            m.flush()
    m.close()


def mostrar_archivo():
    m = open("envios.dat", "rb")
    size = os.path.getsize("envios.dat")
    acu = 0
    cont = 0
    while m.tell() < size:
        envio = pickle.load(m)
        acu += envio.monto
        cont += 1
        print(to_string(envio))

    avg = 0
    if cont > 0:
        avg = round(acu / cont, 2)
    print("El promedio de montos de los envíos que se mostraron fue $", avg)


def test():
    print("Programa de Envíos")
    envios = []
    carga = False
    op = -1

    while op != 6:
        print()
        op = menu_de_opciones()
        print()

        if op == 1:
            print("Carga de Arreglo")
            n = validar_mayor_que(0, "Ingrese el número de envíos a cargar: ")
            envios = cargar_arreglo(envios, n)
            print("Arreglo cargado...")
            carga = True

        elif op == 2:
            if carga:
                print("Mostrar envíos cuyo tipo sea mayor a k")
                k = int(input("Ingrese el valor de k: "))
                if k < 29:
                    print("-" * 67, "ENVÍOS", "-" * 67)
                    mostrar_arreglo(envios, k)
                else:
                    print("No existe tipo de envío mayor a k...")
            else:
                print("Error...Primero debe cargar el registro con la opción 1...")

        elif op == 3:
            if carga:
                print("Búsqueda de envío por número de identificación")
                num = int(input("Ingrese el número de identificación a buscar: "))
                pos = busqueda_binaria(envios, num)
                if pos != -1:
                    print("Registro encontrado...")
                    print(to_string(envios[pos]))
                else:
                    print("Registro no encontrado...")

            else:
                print("Error...Primero debe cargar el registro con la opción 1...")

        elif op == 4:
            if carga:
                print("Guardado en Archivo específico")
                x = float(input("Ingrese el monto mínimo: "))
                y = float(input("Ingrese el monto máximo: "))
                crear_archivo(envios, x, y)
                print("Archivo creado...")
            else:
                print("Error...Primero debe cargar el registro con la opción 1...")

        elif op == 5:
            if os.path.exists("envios.dat"):
                print("Mostrar Archivo creado")
                print("-" * 67, "ENVÍOS", "-" * 67)
                mostrar_archivo()
            else:
                print("Error...Primero debe crear el archivo con la opción 4...")

        elif op == 6:
            print("Bye Bye")
        else:
            print("Valor no válido...Intente nuevamente...")


if __name__ == "__main__":
    test()
