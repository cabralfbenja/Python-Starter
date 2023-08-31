print("Programa de opciones con menu")
menu = "\nMenu de Opciones\n" \
       "-----------------------------------------\n" \
       "1 ------ Temperaturas\n" \
       "2 ------ Análisis de Cadena\n" \
       "3 ------ Salir\n" \
       "Ingrese su opcion:"
op = 0
# op 2
cant_car = cant_voc = porc_voc = 0
while op != 3:
    op = int(input(menu))

    if op == 1:
        print("Temperaturas")
        t1 = int(input("Ingrese la temperatura 1:"))
        t2 = int(input("Ingrese la temperatura 2:"))
        t3 = int(input("Ingrese la temperatura 3:"))
        tupla = t2, t3

        men = may = t1
        for i in range(2):
            if tupla[i] < men:
                men = tupla[i]
            if tupla[i] > may:
                may = tupla[i]
        t_total = t1 + t2 + t3
        promedio_t = t_total / 3
        print("La mayor temperatura es:", may)
        print("La menor temperatura es:", men)
        print("El promedio de las temperaturas es", round(promedio_t, 2))

    if op == 2:
        print("Análisis de Texto")
        cadena = input("Ingrese una cadena de caracteres:")
        for car in cadena:
            cant_car += 1
            if car in "aeiouAEIOU":
                cant_voc += 1
        if cant_voc > 0:
            porc_voc = (cant_voc/cant_car)*100
        print("La cantidad de vocales es", cant_voc, " y su porcentaje en la cadena es", round(porc_voc, 2), "%")
        cant_voc = cant_car = 0

    if op < 1 or op > 2:
        print("Opción no válida, intentar nuevamente")
