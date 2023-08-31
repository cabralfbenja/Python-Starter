"""
5. Colegio Profesiones (Tipo Parcial 4)
Un colegio o asociación de profesionales mantiene información sobre sus distintos miembros. Por cada miembro se
registran los campos siguientes: número de dni del profesional (un número entero), nombre del profesional (una cadena),
importe que paga al colegio por mes, tipo de afiliación (un valor entre 0 y 4 incluidos, por ejemplo de la forma 0:
vitalicio, 1: transitorio, 2: indirecto, etc.) y un número que identifica el tipo de trabajo que desempeña (un número
entero entre 0 y 14 incluidos, para indicar (por ejemplo): 0: empleado, 1: jefe o director, 2: administrativo, etc.)
Se pide definir un tipo registro Profesional con los campos que se indicaron, y un programa completo con menú de
opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado). Puede cargar
 los datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede ordenado
  de menor a mayor, según el dni de los profesionales. Se considerará incorrecta la solución basada en cargar el
  arreglo completo y ordenarlo al final.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado).
 Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que
  tiene el importe desactualizado, si es menor a un valor imp (tambien cargado por teclado)

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo
 tipo de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.

6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar
 nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un
 mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación
por cada posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados
 que sean diferentes de 0.

"""
from profesionales import *
import random
import os
import pickle


def menu_de_opciones():
    print()
    print("Menu de Opciones")
    print("1-Cargar")
    print("2-Mostrar")
    print("3-Buscar por DNI")
    print("4-Crear Archivo específico")
    print("5-Mostrar Archivo creado")
    print("6-Buscar por nombre")
    print("7-Generar y mostrar matriz")
    print("8-Salir")
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
        dni = random.randint(0, 99999)
        for i in range(len(m)):
            if a == m[i]:
                a = 1

    return dni


def cargar_ordenado():
    n = validar_mayor_que(0, "Ingrese el número de profesionales: ")
    pros = [] * n
    docs = []
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        dni = generar_sin_repetir(docs)
        nombre = random.choice(letras) + random.choice(letras) + random.choice(letras)
        importe = round(random.uniform(1500, 5000), 2)
        afiliacion = random.randint(0, 4)
        trabajo = random.randint(0, 14)
        profesional = Profesional(dni, nombre, importe, afiliacion, trabajo)
        add_in_order(pros, profesional)
    return pros


def add_in_order(vector, registro):
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].dni == registro.dni:
            pos = c
            break

        if vector[c].dni < registro.dni:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def mostrar_arreglo(v):
    for registro in v:
        print(to_string(registro))


def busqueda_binaria(pros, dni):
    izq = 0
    der = len(pros) - 1

    while izq <= der:
        c = (izq + der) // 2
        if pros[c].dni == dni:
            return c
        if pros[c].dni < dni:
            izq = c + 1
        else:
            der = c - 1
    return -1


def crear_archivo(pros, x):
    m = open("pros.dat", "wb")
    for i in range(len(pros)):
        if pros[i].trabajo in (3, 4, 5) and pros[i].importe > x:
            pickle.dump(pros[i], m)
            m.flush()
    m.close()


def mostrar_archivo():
    m = open("pros.dat", "rb")
    size = os.path.getsize("pros.dat")
    while m.tell() < size:
        pro = pickle.load(m)
        print(to_string(pro))
    m.close()


def busqueda_secuencial(pros, nom):
    for i in range(len(pros)):
        if pros[i].nombre == nom:
            return i
    return -1


def crear_matriz(pros):
    matriz = [[0] * 5 for f in range(15)]

    for i in range(len(pros)):
        fila = pros[i].trabajo
        columna = pros[i].afiliacion
        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                print("Trabajo:", i, "--- Afiliación:", j, "--- Cantidad:", m[i][j])
        print()

def test():
    print("Sistema de Colegio de Profesiones")
    op = -1
    pros = []
    carga = creado = False

    while op != 8:
        op = menu_de_opciones()
        print()

        if op == 1:
            pros = cargar_ordenado()
            carga = True
            print("Carga completada...")

        else:
            if carga:
                if op == 2:
                    print("-" * 30, "Listado Completo", "-" * 30)
                    mostrar_arreglo(pros)
                elif op == 3:
                    print("Búsqueda por documento")
                    dni = int(input("Ingrese dni a buscar: "))
                    imp = float(input("Ingrese el importe para chequear: "))
                    pos = busqueda_binaria(pros, dni)
                    if pos != -1:
                        print("Documento encontrado...")
                        print(to_string(pros[pos]))
                        if pros[pos].importe < imp:
                            print("El importe está desactualizado...")
                    else:
                        print("Documento no encontrado...")
                elif op == 4:
                    print("Creación de Archivo")
                    x = float(input("Ingrese el importe mínimo para la carga: "))
                    crear_archivo(pros, x)
                    creado = True
                    print("Archivo generado...")
                elif op == 5:
                    if creado:
                        mostrar_archivo()
                    else:
                        print("El archivo no ha sido creado... genérelo con la opción 4")
                elif op == 6:
                    print("Búsqueda por nombre")
                    nom = input("Ingrese el nombre a buscar: ")
                    pos = busqueda_secuencial(pros, nom)
                    if pos != -1:
                        print("Profesional encontrado...")
                        print(to_string(pros[pos]))
                    else:
                        print("Profesional no encontrado...")
                elif op == 7:
                    print("Cantidad de profesionales por cada tipo de afiliación y trabajo")
                    matriz = crear_matriz(pros)
                    mostrar_matriz(matriz)

            elif not carga and op in range(1, 9):
                print("Debe crear el arreglo antes de realizar otra función")
            if op == 8:
                print("Bye Bye")
            elif op not in range (1, 9):
                print("Intente nuevamente...")



if __name__ == "__main__":
    test()
