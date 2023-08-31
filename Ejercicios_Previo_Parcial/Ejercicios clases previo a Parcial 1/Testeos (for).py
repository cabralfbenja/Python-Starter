import random
# Ingreso datos
print("Resultados de Testeos de Covid")
n = int(input("Ingrese cantidad de testeos realizados: "))

cant_positivo = cant_negativo = cant_repetir = 0
edad_acu = 0

for i in range(n):
    print("\nTest", i+1)
    # Ingreso de resultado
    # while res < 1 or res > 3:
        # res = int(input("Ingrese el resultado(1-Positivo, 2-Negativo, 3-Repetir):"))
        # if res < 1 or res > 3:
            # print("Ingreso un dato erróneo")
    # Ingreso de edad
    # while edad <= 0 or edad > 120:
        # edad = int(input("Ingrese la edad (entre 0 y 120 años):"))
        # if edad <= 0 or edad > 120:
            # print("Edad errónea, debe estar entre 0 y 120 años")
    edad = random.randint(18, 65)
    res = random.randint(1, 3)

    print("Edad:", edad)
    print("Resultado:", res)
    # Contabilizar resultado
    if res == 1:
        cant_positivo += 1
    elif res == 2:
        cant_negativo += 1
    else:
        cant_repetir += 1
    # Acumular edad
    edad_acu += edad
    # Reiniciar res y edad
    res = edad = 0

if n > 0:
    promedio_edad = edad_acu / n
    porc_positivo = (cant_positivo / n) * 100
else:
    promedio_edad = 0
    porc_positivo = 0

# Resultados
print("\nLa cantidad de testeos positivos es", cant_positivo)
print("La cantidad de testeos negativos es", cant_negativo)
print("La cantidad de testeos a repetir es", cant_repetir)
print("\nEl porcentaje de positivos con respecto al total es", str(porc_positivo) + "%")
if cant_repetir >= n/2:
    print("Revisar proceso")
print("La edad promedio es", promedio_edad, "años")
