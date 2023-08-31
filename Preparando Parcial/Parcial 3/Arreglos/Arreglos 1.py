# Se pide gestionar las notas de los n alumnos de un curso en un parcial. Para ello se pide:
#
# 1) Ingresar en un arreglo las n notas, n se ingresa por teclado. Las notas son un valor entre 0 y 10.
# 2) Determinar la nota promedio obtenida.
# 3) Mostrar índice y nota de alumnos que obtuvieron una nota mayor al promedio.
# 4) Determinar la nota promedio entre los que aprobaron el parcial (se aprueba con nota >= 4)
# 5) Buscar la menor nota (si hubiera más de una, responder sólo una).
def validar_rango(inf, sup, mensaje):
    valor = inf - 1
    while valor < inf or valor > sup:
        valor = int(input(mensaje))
        if valor < inf or valor > sup:
            print("Valor no válido...")
    return valor


def cargar_vector(notas):
    for i in range(len(notas)):
        notas[i] = validar_rango(0, 10, "Ingrese la nota del alumno: ")


def promedio_vector(notas):
    cant = len(notas)
    suma = 0
    for i in range(cant):
        suma += notas[i]
    prom = suma / cant
    return prom


def mostrar_mayores(notas, prom):
    for i in range(len(notas)):
        if notas[i] > prom:
            print("Posición:", i, "- Nota:", notas[i])


def promedio_aprobados(notas):
    cant = 0
    suma = 0
    for i in range(len(notas)):
        if notas[i] >= 4:
            suma += notas[i]
            cant += 1
    prom = 0
    if cant > 0:
        prom = suma / cant
    return prom


def buscar_menor(notas):
    pos_menor = 0
    for i in range(1, len(notas)):
        if notas[i] < notas[pos_menor]:
            pos_menor = i
    return pos_menor

def principal():
    print("Registro de Notas de Alumnos")
    n = int(input("Ingrese el número de alumnos del curso: ")) # VALIDAR > 0
    notas = [0] * n

    cargar_vector(notas)
    print(notas)

    prom = promedio_vector(notas)
    print("Promedio:", prom)

    mostrar_mayores(notas, prom)

    prom_aprobados = promedio_aprobados(notas)
    print("Promedio de los Aprobados:", prom_aprobados)

    pos_menor = buscar_menor(notas)
    print("Menor Nota: ", notas[pos_menor], " - Posición: ", pos_menor)



if __name__ == "__main__":
    principal()



