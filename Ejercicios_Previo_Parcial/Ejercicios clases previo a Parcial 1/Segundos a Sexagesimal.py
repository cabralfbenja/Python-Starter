print("Conversor en Ángulo Sexagesimal")

# Ingreso
r_seg = int(input("Ingrese su ángulo en segundos:"))

# Proceso
grados = r_seg // 3600
resto_grados = r_seg % 3600
minutos = resto_grados // 60
segundos = resto_grados % 60


# Resultados
print("Su ángulo en sexagesimal es:", str(grados) + "°", str(minutos) + "'", str(segundos) + "\"")
