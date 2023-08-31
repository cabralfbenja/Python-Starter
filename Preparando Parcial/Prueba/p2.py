print("Progrma de menú de opciones")
op = 0
# Opción 1
num = 1
cont_rango = suma = promedio = 0
cant_pares = 0
# Opción 2
c1 = c2 = c3 = -1
c_sup = 0
total_granos = 0

menu = "Menu de Opciones\n" \
       "-----------------------------------------\n" \
       "1 ------ Procesar secuencia de numeros\n" \
       "2 ------ Produccion de Granos\n" \
       "3 ------ Salir\n" \
       "Ingrese su opcion:"

while op != 3:
    op = int(input(menu))

    if op == 1:
        print("\nAnálisis de secuencia de números")
        while num != 0:
            num = int(input("Ingrese un número (La carga termina con 0):"))
            if 15 <= num <= 25:
                cont_rango += 1
                suma += num
            if num % 2 == 0:
                cant_pares += 1
        if cont_rango > 0:
            promedio = suma / cont_rango

        print("El acumulado total de todos los números que están entre 15 y 25:", suma)
        print("La cantidad de números pares:", cant_pares)
        print("El promedio de los valores acumulados de los números entre 15 y 25:", promedio)
        print("La cantidad de números entre 15 y 25:", cont_rango)

    if op == 2:
        print("Producción de granos")
        while c1 < 0:
            c1 = int(input("Ingrese cuántas toneladas de granos produjo la provincia 1:"))
            if c1 < 0:
                print("Cantidad ingresada no válida...\n")

        while c2 < 0:
            c2 = int(input("Ingrese cuántas toneladas de granos produjo la provincia 2:"))
            if c2 < 0:
                print("Cantidad ingresada no válida...\n")

        while c3 < 0:
            c3 = int(input("Ingrese cuántas toneladas de granos produjo la provincia 3:"))
            if c3 < 0:
                print("Cantidad ingresada no válida...\n")

        total_granos = c1 + c2 + c3

        prom_granos = total_granos / 3

        t = (c1, c2, c3)
        for i in range(3):
            if t[i] > prom_granos:
                c_sup += 1
        print("Granos promedio:", round(prom_granos, 2))
        print("Cantidad de valores superiores al promedio:", c_sup)
    if op < 1 or op > 3:
        print("Opción no válida...\n")
print("Fin del programa")
