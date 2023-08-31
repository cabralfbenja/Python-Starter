print("Programa de menú de opciones")
op = 0
time = -1
clt = cp = cj = 0
porcentaje_p = porcentaje_j = 0

while op > 2 or op < 1:
    print("Escoja la opción que desee")
    print("1)Atletas y tiempos")
    print("2)Análisis de texto")
    op = int(input("Opción:"))
    if op > 2 or op < 1:
        print("Opción no válida, intente nuevamente...\n")
if op == 1:
    print("\nAtletas y tiempos")
    name = input("Nombre del atleta 1:")
    while time < 0:
        time = int(input("Ingrese el tiempo del atleta 1 (en segundos):"))
        if time < 0:
            print("Tiempo negativo o nulo, no es válido...")
    men = time
    men_nom = name
    time = -1
    for i in range(0, 2):
        name = input("Nombre del atleta " + str(i+2)+":")
        while time < 0:
            time = int(input("Ingrese el tiempo del atleta " + str(i+1)+" (en segundos):"))
            if time < 0:
                print("Tiempo negativo o nulo, no es válido...")
        if time < men:
            men = time
            men_nom = name
        time = -1
    print("El ganador es", men_nom)
    if men < 850:
        print("Ha batido un record con un tiempo de", men, "segundos")

if op == 2:
    texto = input("\nIngrese un texto (termina con punto):")
    for car in texto:
        clt += 1
        if car == "p":
            cp += 1
        if car == "j":
            cj += 1
        if car == ".":
            break
    print("Cantidad de letras 'p':", cp)
    print("Cantidad de letras 'j':", cj)
    if cp > 0:
        porcentaje_p = (cp / clt) * 100
    if cj > 0:
        porcentaje_j = (cj / clt) * 100

    print("Porcentaje de letras 'p':", round(porcentaje_p, 2), "%")
    print("Porcentaje de letras 'j':", round(porcentaje_p, 2), "%")
print("\nFin del Programa")
