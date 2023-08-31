import apuesta

def validar(inf):
    n = int(input("Valor (mayor a "+ str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error...se pidió > " + str(inf) + " ...Cargue de nuevo: "))
    return n

def validar_cab(mn, mx):
    cab = int(input("Ingrese caballo (>= " + str(mn) + " y <= " + str(mx) +"): "))
    while cab < mn or cab > mx:
        cab = int(input("Error...se pidió(>= " + str(mn) + " y <= " + str(mx) +"). De nuevo: "))
    return cab


def read(bet):
    n = len(bet)
    for i in range(n):
        num = int(input("Ingrese número de Ticket[" + str(i) + "] : "))
        print("Ingrese caballo elegido (0 a 9)")
        cab = validar_cab(0, 9)
        print("Ingrese monto a apostar")
        monto = validar(0)

        bet[i] = apuesta.Apuesta(num, cab, monto)
        print()

def montos_totales(bet):
    c = [0] * 10
    for apuesta in bet:
        horse = apuesta.caballo
        monto = apuesta.monto
        c[horse] += monto
    return c

def opcion1(bet):
    print("Monto total por caballo")
    caballo = montos_totales(bet)
    for i in range(len(caballo)):
        print("Monto total del caballo ", i, ": ", caballo[i])


def search(bet, t):
    for apuesta in bet:
        if apuesta.numero == t:
            apuesta.monto *= 10
            return apuesta
    return None

def opcion2(bet, ticket):
    b = search(bet, ticket)

    if b is not None:
        print(apuesta.to_string(b))
    else:
        print("No existe una apuesta con ese ticket...")


def test():
    print("Hipódromo")
    print("¿Cuántas apuestas se realizaron?")
    n = validar(0)
    bet = [None] * n

    op = -1
    print("Cargue los datos de las apuestas\n")
    read(bet)

    while op != 5:
        print("\nMenu de opciones:")
        print("1. Monto total por caballo")
        print("2. Buscar Ticket")
        print("3. Contabilización de apuesta para un caballo")
        print("4. Mostrar los datos del ticket con mayor monto apostado")
        print("5. Salir")
        op = int(input("Ingrese elección: "))
        if op == 1:
            opcion1(bet)
        elif op == 2:
            print("Búsqueda y modificación de Ticket")
            ticket = int(input("Ticket a buscar: "))
            opcion2(bet, ticket)

        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            print("Bye Bye")
        else:
            print("Valor no válido.\n")

if __name__ == "__main__":
    test()
