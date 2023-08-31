# Ingreso de Datos
dato_u = int(input("Ingrese cantidad de segundos:"))

# Proceso
segundos = dato_u % 60
minutos = (dato_u // 60) % 60
horas = dato_u // 3600

# Resultados
print("Su resultado en horas:minutos:segundos :")
print(horas, ":", minutos, ":", segundos)
