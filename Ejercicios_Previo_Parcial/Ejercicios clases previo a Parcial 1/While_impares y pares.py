print("Números pares e impares")

numero = int(input("Ingrese un número (negativo si quiere frenar):"))
par, impar, suma = 0, 0, 0
cero = False
estan_alternado = True
anterior = 2
while numero >= 0:
    # Paridad
    paridad = numero % 2
    if paridad == 0:
        par += 1
    else:
        impar += 1
# Suma de números entre 50 y 100
    if 50 <= numero <= 100:
        suma += numero
# Número igual a cero?
    if numero == 0:
        cero = True
# Valores alternados?
    if paridad == anterior:
        estan_alternado = False
    anterior = paridad
    numero = int(input("Ingrese un número (negativo si quiere frenar):"))

print("La cantidad de pares fue:", par)
print("La cantidad de impares fue:", impar)
print("La suma de números entre 50 y 100:", suma)
if cero:
    print("Se ingresó un cero")
else:
    print("No se ingresó un cero")
if estan_alternado:
    print("La secuencia sigue un patrón alternado de pares e impares")
else:
    print("La secuencia no sigue un patrón alternado de pares e impares")
