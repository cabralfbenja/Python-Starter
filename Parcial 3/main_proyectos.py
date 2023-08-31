import proyecto
import random


def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Cargar")
    print("2-Mostrar")
    print("3-Monto de honorarios por tipo de proyecto")
    print("4-Proyectos de cualquier tipo menos el 4")
    print("5-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def monto_tipo(proyectos):
    montos = [0] * 15

    for i in range(len(proyectos)):
        montos[proyectos[i].tipo] += proyectos[i].honorarios

    for i in range(len(montos)):
        print("Tipo: ", i, "--- Monto Total:", round(montos[i], 2))


def honorarios_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].honorarios > v[j].honorarios:
                v[i], v[j] = v[j], v[i]


def carga(proyectos):
    nombres = ("Juan", "Carlos", "Alberto", "Esteban", "María", "Juana", "Mirtha", "Benjamín")
    apellidos = ("Cabral", "Farré", "Juncos", "Bergero", "Masanés", "Gutierrez", "Gorsd")
    for i in range(len(proyectos)):
        num = random.randint(0, 1000)
        cliente = random.choice(nombres) + " " + random.choice(apellidos)
        hon = round(random.uniform(1000, 5000), 2)
        tipo = random.randint(0, 14)

        proyectos[i] = proyecto.Proyecto(num, cliente, hon, tipo)


def mostrar(proyectos):
    for p in proyectos:
        print(proyecto.to_string(p))


def mostrar_s4(proyectos):
    for p in proyectos:
        if p.tipo != 4:
            print(proyecto.to_string(p))


def test():
    print("Estudio de Arquitectura")
    proyectos = []
    op = -1
    charge = False
    while op != 5:
        print()
        op = menu_de_opciones()

        if op == 1:
            print("Carga")
            n = validar_mayor_que(0, "Ingrese cantidad de proyectos a cargar: ")
            proyectos = [0] * n
            carga(proyectos)
            charge = True

        elif op == 2:
            if not charge:
                print("Realice primero la carga...Opción 1")
            else:
                print("-" * 30, "Proyectos", "-" * 30)
                mostrar(proyectos)
        elif op == 3:
            if not charge:
                print("Realice primero la carga...Opción 1")
            else:
                print("Monto por tipo de proyecto:")
                monto_tipo(proyectos)
        elif op == 4:
            if not charge:
                print("Realice primero la carga...Opción 1")
            else:
                honorarios_sort(proyectos)
                mostrar_s4(proyectos)
        elif op == 5:
            print("Bye Bye")
        else:
            print("Valor no válido")


if __name__ == "__main__":
    test()
