def validar_rango(inf, sup, mensaje):
    valor = inf - 1
    while valor < inf or valor > sup:
        valor = int(input(mensaje))
        if valor < inf or valor > sup:
            print("Valor no válido...")
    return valor


def titulo_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].titulo < v[j].titulo:
                v[i], v[j] = v[j], v[i]

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

def porcentaje(subtotal, total):
    pct = (subtotal / total) * 100

    return round(pct, 2)

def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor

def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


# Cargas
def cargar_vector(v, n):
    for i in range(n):
        num = random.randint(1, 100)
        tit = "Título " + str(num)
        imp = random.uniform(1000, 30000000)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)
        peli = pelicula.Pelicula(num, tit, imp, tipo, pais)
        add_in_order(v, peli)

def add_in_order(vector, registro):
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].titulo == registro.titulo:
            pos = c
            break

        if vector[c].titulo < registro.titulo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def generar_sin_repetir(m):
    a = 1
    while a == 1:
        a = 0
        votante = random.randint(0, 99999)
        for i in range(len(m)):
            if a == m[i]:
                a = 1

    return votante

# Búsquedas

def busqueda_binaria(peliculas, nom):
    izq = 0
    der = len(peliculas) - 1

    while izq <= der:
        c = (izq + der) // 2
        if peliculas[c].titulo == nom:
            return c
        if peliculas[c].titulo < nom:
            izq = c + 1
        else:
            der = c - 1
    return -1


def busqueda_secuencial(pros, nom):
    for i in range(len(pros)):
        if pros[i].nombre == nom:
            return i
    return -1

# Matriz
# Generar Matriz de Conteo
def generar_matriz(v):
    mat = [[0] * 15 for i in range(5)]
    for prof in v:
        f = prof.afiliacion
        c = prof.tipo
        mat[f][c] += 1
    return mat


# Mostrar Matriz de Conteo
def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > 0:
                print("Para el tipo de afiliación {} y el tipo de trabajo {} hay {} profesionales".format(f, c, mat[f][c]))

# Menu
def menu_de_opciones():
    print("Menu de Opciones")
    print("1-Cargar")
    print("2-Mostrar")
    print("3-")
    print("4-")
    print("5-")
    print("6-Salir")
    print()
    op = int(input("Ingrese opción deseada: "))

    return op
