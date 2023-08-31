import random
import prenda


def validar_mayor_que(inf):
    n = int(input("Valor (mayor a " + str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error...se pidió > " + str(inf) + " ...Cargue de nuevo: "))
    return n


def cargar(prendas):
    descripcion = ("Suelta", "Lisa", "Rota", "Elongada", "Chica", "Grande")
    descripcion2 = ("Blanca", "Roja", "Verde", "Azul", "Violeta", "Amarillo")
    for i in range(len(prendas)):
        numero = random.randint(1, 500)
        desc = random.choice(descripcion) + " " + random.choice(descripcion2)
        precio = random.randint(300, 2000)
        stock = random.randint(20, 200)
        tipo = random.randint(0, 14)
        prendas[i] = prenda.Prenda(numero, desc, precio, stock, tipo)


def ordenar(prendas):
    n = len(prendas)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if prendas[j].tipo < prendas[i].tipo:
                prendas[i], prendas[j] = prendas[j], prendas[i]


def mostrar(prendas):
    for i in range(len(prendas)):
        print(prenda.to_string(prendas[i]))


def contador_stock(prendas):
    v = [0] * 15
    for i in range(len(prendas)):
        v[prendas[i].tipo] += prendas[i].stock

    return v


def mostrar_stock(stock):
    for i in range(len(stock)):
        if stock[i] != 0:
            print("Tipo: ", i, " --- Cantidad:", stock[i])


def buscar_mayor(prendas):
    mayor = 0
    for i in range(1, len(prendas)):
        if prendas[i].precio > prendas[mayor].precio:
            mayor = i
    return mayor


def buscar_desc(prendas, x):
    encontrado = False
    for i in range(len(prendas)):
        if prendas[i].descripcion == x:
            print(prenda.to_string(prendas[i]))
            importe = prendas[i].precio * prendas[i].stock
            print("Importe: $", importe)
            encontrado = True
    if not encontrado:
        print("No se encontró una prenda con la descripción dada.")


def test():
    print("Tienda de Ropa")
    prendas = []
    op = -1

    charge = False
    while op != 6:
        print()
        print("Prendas - Menú de Opciones")
        print("Opción 1: Cargar")
        print("Opción 2: Ordenar y Mostrar")
        print("Opción 3: Contador de stock por tipo")
        print("Opción 4: Prenda de mayor precio")
        print("Opción 5: Búsqueda por descripción")
        print("Opción 6: Salir")

        op = int(input("Ingrese su opción: "))

        if op == 1:
            print("Ingrese cantidad de prendas")
            n = validar_mayor_que(0)
            prendas = [0] * n
            cargar(prendas)
            charge = True

        elif op == 2:
            if not charge:
                print("No se ha realizado la carga...")
            else:
                ordenar(prendas)
                mostrar(prendas)

        elif op == 3:
            if not charge:
                print("No se ha realizado la carga...")
            else:
                stock_p = contador_stock(prendas)
                mostrar_stock(stock_p)

        elif op == 4:
            if not charge:
                print("No se ha realizado la carga...")
            else:
                mayor_precio = buscar_mayor(prendas)
                print(prenda.to_string(prendas[mayor_precio]))

        elif op == 5:
            if not charge:
                print("No se ha realizado la carga...")
            else:
                x = input("Ingrese la descripción de la prenda buscada: ")
                buscar_desc(prendas, x)
        elif op == 6:
            print("\nBye Bye")

        else:
            print("Opción no válida...intente nuevamente.")


if __name__ == "__main__":
    test()
