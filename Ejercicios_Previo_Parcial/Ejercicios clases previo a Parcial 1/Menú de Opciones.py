import random

op = 0
num = None
suma = i = 0
n = -1
positivos = negativos = 0
nota = -1

while op != 4:
    print("\nIngrese su opción deseada\n1.Calcular de Promedio\
                \n2.Cantidad de positivos y negativos\
                \n3.Evaluar alumno\
                \n4. Salir")
    op = int(input("Opción:"))

    if op == 1:
        print("\nOpción 1")
        num = int(input("Ingrese un número (la carga finaliza cuando se ingresa el -1):"))
        while num != -1:
            suma += num
            i += 1
            num = int(input("Ingrese un número (la carga finaliza cuando se ingresa el -1):"))
        if i != 0:
            prom = suma / i
        else:
            prom = 0
        print("El promedio de los números ingresados es:", prom)
        suma = i = 0

    elif op == 2:
        print("\nOpción 2")
        while n < 0:
            n = int(input("Ingrese cantidad de vueltas a dar:"))
            if n < 0:
                print("No ingresó un valor válido")
        for j in range(n):
            x = random.randint(-100, 100)
            if x > 0:
                positivos += 1
            elif x < 0:
                negativos += 1
        print("La cantidad de positivos es:", positivos)
        print("La cantidad de negativos es:", negativos)
        positivos = negativos = 0

    elif op == 3:
        print("\nOpción 3")
        print("Ingrese su notas para saber su condición")
        while nota < 0 or nota > 10:
            nota = int(input("Ingrese su nota:"))
            if nota < 0 or nota > 10:
                print("Ingresó una nota no válida")
        if nota >= 4:
            print("Usted está APROBADO")
        else:
            print("Usted está LIBRE")
        nota = -1
    elif op == 4:
        print("Bye-Bye")
    else:
        print("Opción incorrecta")
    op = 0
print("Fin del programa")
