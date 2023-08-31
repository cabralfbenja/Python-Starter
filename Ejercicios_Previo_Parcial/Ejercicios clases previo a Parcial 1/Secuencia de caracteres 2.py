print("Programa de Secuencia de caractéres")

# Cantidad total de palabras
ctp = 0
# Contador de letras por palabras
cl = 0
# Acumulador de letras
acum_letras = 0

# Flag de hay m
hay_m = False
# Flag de hay mo
smo = 0
cant_mo = 0

# Contador de palabras > 4 letras
cp4 = 0

# Flag de hay x o y
hay_xy = False
cant_xy = 0

# Carga del texto completo
cadena = input("Cargue el texto (termina con punto):")

for car in cadena:
    # Palabra termina
    if car == " " or car == ".":
        acum_letras += cl
        if cl > 1:
            ctp += 1
        if cl > 4:
            cp4 += 1
        if hay_xy:
            cant_xy += 1
        if smo == 1:
            cant_mo += 1

        # Reiniciamos las variables
        hay_xy = False
        hay_m = False
        smo = 0
        cl = 0


    else:
        cl += 1
        if car == "x" or car == "y":
            hay_xy = True
        if car in "Mm":
            hay_m = True
        else:
            if hay_m and car == "o":
                smo += 1
            hay_m = False


# Promedio de letras por palabras
if ctp > 0:
    avg_letras = acum_letras / ctp
else:
    avg_letras = 0

print("Cantidad de palabras con más de cuatro letras:", cp4)
print("Cantidad de palabras con 'x' o 'y':", cant_xy)
print("Promedio de letras por palabra:{:.2f}".format(avg_letras))
print("Cantidad de palabras con la expresión 'mo' solo una vez:", cant_mo)
