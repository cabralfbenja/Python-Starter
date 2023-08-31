import random

print("Juego de lanzamiento de dados")

# Lanzamiento
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dados = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print("Dado 1:", dado1)
print("Dado 2:", dado2)
print(sum(dados))
suma = dado1 + dado2

# Comparación
if dado1 == dado2 or suma % 2 == 1:
    ganador = "usuario"
else:
    ganador = "máquina"


print("El ganador fue", ganador)
