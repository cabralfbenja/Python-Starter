"""
1- Cargar: Cargar el contenido del archivo en un vector de registros de libros, que siempre debe mantenerse ordenado por
isbn (Omitir la primera línea del archivo, que contiene el nombre de los campos)

2- Sumar revisión: El usuario puede optar por buscar el libro por ISBN o por título. Según el criterio elegido se debe
ingresar por teclado el ítem a buscar. Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.

3- Mayor revisiones: Buscar en el vector el libro con mayor cantidad de revisiones. Informar si su rating es mayor,
menor o igual al rating promedio de su mismo idioma.

4- Popularidad 2000: A partir del vector, generar una matriz donde cada fila sea un idioma y cada columna un año de
publicación. La celda debe contener el libro que tenga mayor rating para ese idioma y año (si hubiera varios, elegir
sólo uno) sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).

5- Publicaciones por década: A partir del vector, generar un vector de conteo donde cada celda representa una década
entre 1900 y 2000. La celda debe indicar cuántos libros se publicaron en esa década. Mostrar todas las cantidades
mayores a cero. Informar además cuál fue la década con más publicaciones. Si varias tuvieran la misma cantidad,
informar todas.

6- Guardar populares: Si la matriz de la opción 4 ya fue generada, almacenar su contenido registros por registro
(omitiendo las celdas vacías) en un archivo binario llamado populares.dat e informar la cantidad de registros grabados.
Si la matriz aún no fue generada, informarlo.

7- Mostrar archivo: Listar el contenido del archivo generado en el punto anterior.
"""
import pickle
import os
import registro


def menu():
    cad = "MENÚ DE OPCIONES:\n" \
          "1. Cargar\n" \
          "2. Sumar Revisión\n" \
          "3. Mayor revisiones\n" \
          "4. Popularidad 2000\n" \
          "5. Publicaciones por década\n" \
          "6. Guardar populares\n" \
          "7. Mostrar archivo\n" \
          "8. Salir\n" \
          "Opción: "
    return cad


def menu_busqueda():
    cad = "\nDesea buscar el libro según:\n" \
          "1. Título\n" \
          "2. ISBN\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    """
    Esta función valida que un valor númerico entero ingresado por teclado se encuentre entre un límite inferior y uno
    superior.
    :param inf: Límite inferior
    :param sup: Límite superior
    :param mensaje: Mensaje mostrado indicando qué se debe ingresar por teclado
    :return: Valor ingresado por teclado
    """
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def add_in_order(vector, isbn):
    """
    Agregar libro a un vector en orden según ISBN a partir del algoritmo de búsqueda binaria
    :param vector: Vector al que se agrega el libro
    :param isbn: Elemento agregado
    :return: -
    """
    n = len(vector)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].isbn == isbn.isbn:
            pos = c
            break

        if vector[c].isbn < isbn.isbn:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [isbn]


def cargar_archivo(fd):
    v = []
    m = open(fd, "rt", encoding="utf8")
    # Mover el puntero para no imprimir la primer línea
    m.readline()
    for linea in m:
        cadenas = linea.split(',')
        tit = cadenas[0]
        rev = int(cadenas[1])
        year = int(cadenas[2])
        idi = int(cadenas[3])
        rat = float(cadenas[4])
        # Eliminar salto de linea con .rstrip()
        isbn = cadenas[5].rstrip()
        lib = registro.Libro(tit, rev, year, idi, rat, isbn)
        add_in_order(v, lib)
    return v


def busqueda_titulo(v, x):
    pos = -1
    for i in range(len(v)):
        if x == v[i].titulo:
            pos = i
            return pos
    return pos


def busqueda_isbn(libros, x):
    izq = 0
    der = len(libros) - 1

    while izq <= der:
        c = (izq + der) // 2
        if libros[c].isbn == x:
            return c
        if libros[c].isbn < x:
            izq = c + 1
        else:
            der = c - 1
    return -1


def promedio(total, cantidad):
    prom = 0
    # Evitar n/0
    if cantidad > 0:
        prom = round(total / cantidad, 2)
    return prom


def may_men_ig(may, proms):
    if may.rating > proms[may.idioma-1]:
        return "Mayor"
    elif may.rating < proms[may.idioma-1]:
        return "Menor"
    else:
        return "Igual"


# REVISAR MODULARIZACIÓN
def opcion3(v):
    cont = acu = proms = [0] * 27

    may = v[0]
    cont[v[0].idioma-1] += 1
    acu[v[0].idioma-1] += v[0].rating

    for i in range(1, len(v)):

        cont[v[i].idioma - 1] += 1
        acu[v[i].idioma - 1] += v[i].rating

        if v[i].revisiones > may.revisiones:
            may = v[i]

    for i in range(len(proms)):
        proms[i] = promedio(acu[i], cont[i])

    print("\nEl libro con más revisiones fue: ")
    print(registro.to_string(may))
    print("Su rating comparado al promedio de su idioma fue: " + may_men_ig(may, proms))
    print("Rating promedio del idioma {}: {}\n".format(may.idioma, proms[may.idioma-1]))


def generar_matriz(v, filas, columnas):
    mat = [[0] * columnas for i in range(filas)]
    for lib in v:
        if 2000 <= lib.year <= 2020:
            f = lib.idioma - 1
            c = lib.year - 2000
            if mat[f][c] == 0:
                mat[f][c] = lib
            elif mat[f][c].rating < lib.rating:
                mat[f][c] = lib
    return mat


def generar_archivo(mat, fd_b):
    m = open(fd_b, "wb")
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] != 0:
                pickle.dump(mat[f][c], m)
                cont += 1
                m.flush()
    print("\nArchivo creado! Se grabaron {} libros\n".format(cont))
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo!")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        lib = pickle.load(m)
        print(registro.to_string(lib))
    m.close()


def publicaciones_dec(v):
    vd = [0]*10
    for lib in v:
        if 1900 <= lib.year < 1910:
            vd[0] += 1
        elif 1910 <= lib.year < 1920:
            vd[1] += 1
        elif 1920 <= lib.year < 1930:
            vd[2] += 1
        elif 1930 <= lib.year < 1940:
            vd[3] += 1
        elif 1940 <= lib.year < 1950:
            vd[4] += 1
        elif 1950 <= lib.year < 1960:
            vd[5] += 1
        elif 1960 <= lib.year < 1970:
            vd[6] += 1
        elif 1970 <= lib.year < 1980:
            vd[7] += 1
        elif 1980 <= lib.year < 1990:
            vd[8] += 1
        elif 1990 <= lib.year < 2000:
            vd[9] += 1
    return vd


def mostrar_vc(vc):
    for i in range(len(vc)):
        print("El nro. de libros publicados en la decada de {} fue {}".format((i*10 + 1900), vc[i]))


def buscar_mayor(vc):
    may = [0]
    for i in range(1, len(vc)):
        if vc[i] > may[0]:
            may = [i]
        elif vc[i] == may[0]:
            may.append(i)
    return may


def test():
    op = -1
    fd = "libros.csv"
    fd_b = "populares.dat"
    exist_v = False
    exist_mat = False
    v = []
    mat = []

    while op != 8:
        op = validar_entre(1, 8, menu())

        if op == 1:
            v = cargar_archivo(fd)
            exist_v = True
            print("\nArreglo Cargado!\n")
        elif op == 2:
            if exist_v:

                print(registro.to_string(v[125]))
                op2 = validar_entre(1, 2, menu_busqueda())
                if op2 == 1:
                    # Busqueda por título
                    x = str(input("\nIngrese el título del libro a buscar: "))
                    pos = busqueda_titulo(v, x)
                    if pos != -1:
                        # Mostrar libro
                        print("Se ha encontrado el libro buscado: Se le ha sumado una revisión")
                        v[pos].revisiones += 1
                        print(registro.to_string(v[pos]))
                        print()
                    else:
                        print("No se ha encontrado el libro buscado")
                else:
                    # Busqueda por ISBN: NO FUNCIONA
                    x = input("\nIngrese el ISBN del libro a buscar: ")
                    pos = busqueda_isbn(v, x)
                    if pos != -1:
                        # Mostrar libro
                        print("Se ha encontrado el libro buscado: Se le ha sumado una revisión")
                        v[pos].revisiones += 1
                        print(registro.to_string(v[pos]))
                        print()
                    else:
                        print("No se ha encontrado el libro buscado\n")
            else:
                print("\nERROR... No existe arreglo! Pruebe crearlo con la opción 1\n")
        elif op == 3:
            if exist_v:
                opcion3(v)
            else:
                print("\nERROR... No existe arreglo! Pruebe crearlo con la opción 1\n")
        elif op == 4:
            if exist_v:
                mat = generar_matriz(v, 27, 21)
                print("\nMatriz Generada!\n")
                exist_mat = True
            else:
                print("\nERROR... No existe arreglo! Pruebe crearlo con la opción 1\n")
        elif op == 5:
            if exist_v:
                print("\nPublicaciones por década:\n")
                vc_dec = publicaciones_dec(v)
                mostrar_vc(vc_dec)
                x = buscar_mayor(vc_dec)
                print("\nLa/s decadas con más publicaciones fueron: ")
                for dec in x:
                    print("Decada del {}\n".format(dec*10 + 1900))
            else:
                print("\nERROR... No existe arreglo! Pruebe crearlo con la opción 1\n")
        elif op == 6:
            if exist_mat:
                generar_archivo(mat, fd_b)
            else:
                print("\nERROR... No existe matriz! Pruebe crearla con la opción 4\n")
        elif op == 7:
            print("\nLibros:")
            mostrar_archivo(fd_b)
            print()


if __name__ == "__main__":
    test()
