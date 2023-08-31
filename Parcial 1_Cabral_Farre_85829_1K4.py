# Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes
# opciones:
#
# 1.)    Ingrese por teclado la cantidad de pasajeros de tres aviones, y el identificador o nombre
# de cada vuelo (una cadena de caracteres para cada vuelo) e informe el identifcador del vuelo con
# la menor cantidad de pasajeros y cuál es la cantidad promedio entre los tres vuelos. Muestre la
#  diferencia entre el promedio y la cantidad menor.
#
# 2.)    Ingrese por teclado una secuencia de números enteros, a razón de uno por vuelta de ciclo.
# La carga finaliza cuando el usuario ingresa un cero. Determine cuántos han sido pares y cuántos impares.
# Indique al final si la cantidad del pares es mayor, menor o igual que la cantidad de impares.
#
# 3.)    Terminar el programa.

print("Parcial 1")
print("Programa de opciones con menu")

menu = "\nMenu de Opciones\n" \
       "1 --- Aviones y pasajeros \n" \
       "2 --- Secuencia de números\n" \
       "3 --- Salir\n" \
       "Ingrese su opcion:"

op = 0
while op != 3:
    op = int(input(menu))

    if op == 1:
        print("\nAviones y pasajeros")
        print("Ingrese el identificador del vuelo y la cantidad de pasajeros correspondiente")

        # CARGA de DATOS
        vuelo1 = input("\nIdentificador del vuelo:")
        cant_p1 = int(input("Cantidad de pasajeros:"))
        vuelo2 = input("\nIdentificador del vuelo:")
        cant_p2 = int(input("Cantidad de pasajeros:"))
        vuelo3 = input("\nIdentificador del vuelo:")
        cant_p3 = int(input("Cantidad de pasajeros:"))

        # MENOR
        if cant_p1 < cant_p2 and cant_p1 < cant_p3:
            menor = vuelo1
            cant_menor = cant_p1
        elif cant_p2 < cant_p3:
            menor = vuelo2
            cant_menor = cant_p2
        else:
            menor = vuelo3
            cant_menor = cant_p3

        # PROMEDIO y DIFERENCIA
        promedio = (cant_p1 + cant_p2 + cant_p3) / 3

        diferencia = promedio - cant_menor

        # RESULTADOS
        print("\nEl vuelo con la menor cantidad de pasajeros fue", menor)
        print("La cantidad promedio de pasajeros entre los 3 vuelos fue", round(promedio, 2))
        print("La diferencia entre el promedio y la cantidad más pequeña fue de", round(diferencia, 2))

    elif op == 2:
        # CONTADORES
        cont_par = cont_impar = 0

        print("\nSecuencia de números")

        # CARGA de NÚMEROS
        num = int(input("Ingrese un número (termina con cero):"))
        while num != 0:
            if num % 2 == 0:
                cont_par += 1
            else:
                cont_impar += 1
            num = int(input("Ingrese un número (termina con cero):"))

        # RESULTADOS de CANTIDADES
        print("\nCantidad de números pares:", cont_par)
        print("Cantidad de números impares:", cont_impar)

        # COMPARACIÓN
        if cont_par > cont_impar:
            print("La cantidad de pares es mayor a la de impares")
        elif cont_par < cont_impar:
            print("La cantidad de pares es menor a la de impares")
        else:
            print("La cantidad de pares es igual a la de impares")

    elif op == 3:
        print("Programa finalizado")

    else:
        print("Opción no válida, intente nuevamente\n")
