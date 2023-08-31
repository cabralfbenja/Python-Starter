print("Calculadora de Pintrura")
# Ingreso de datos
altura = float(input("Ingrese la altura de su pared(en metros):"))
ancho = float(input("Ingrese el ancho de su pared(en metros):"))

# Proceso
superficie = altura * ancho
cant_pintura = superficie / 10
cant_pintura_int = superficie // 10

# Mostrar resultados
print("La cantidad de pintura necesaria son", cant_pintura, "litros")
print("La cantidad de pintura entera necesaria son", cant_pintura_int, "litros")
