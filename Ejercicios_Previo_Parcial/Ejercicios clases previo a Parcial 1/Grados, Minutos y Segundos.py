print("Conversor de Ángulo Sexagesimal")

# Ingreso
grados = int(input("Ingrese grados:"))
minutos = int(input("Ingrese minutos:"))
segundos = int(input("Ingrese segundos:"))

# A grados
min_en_grados = minutos / 60
seg_en_grados = segundos / 3600
r_grados = grados + min_en_grados + seg_en_grados

# A minutos
grados_en_minutos = grados * 60
seg_en_minutos = segundos / 60
r_minutos = grados_en_minutos + minutos + seg_en_minutos

# A segundos
grados_en_seg = grados * 3600
minutos_en_seg = minutos * 60
r_seg = grados_en_seg + minutos_en_seg + segundos

# Resultados
print("Ángulo en grados:", str(round(r_grados, 2)) + "°")
print("Ángulo en minutos:", str(round(r_minutos, 2)) + "'")
print("Ángulo en segundos:", str(r_seg) + "\"")
