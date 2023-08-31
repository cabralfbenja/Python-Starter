print("Programa de Secuencia de caractéres")

# Cantidad total de palabras
ctp = 0

# Cantidad de palabras que inician con p
cpp = 0

# Contador de palabras que contienen ta
cta = 0

# Contador de letras por palabras
cl = 0
# Flag de hay t
hay_t = False
# Flag de hay ta
sta = False
# Carga del texto completo
cadena = input("Cargue el texto (termina con punto):")

for car in cadena:
    cl += 1

    if car == " " or car == ".":
        # Analizar lo que pasó con la palabra que terminó
        if cl > 1:
            # Contabilizar palabra
            ctp += 1
        if sta:
            cta += 1

        # Volver a cero cl
        cl = 0
        hay_t = False
        sta = False
    else:
        # Tengo una letra y estoy dentro de la palabra actual

        if car in "pP" and cl == 1:
            cpp += 1
        # Detectar secuencia ta
        if car == "t":
            hay_t = True
        else:
            if car == "a" and hay_t:
                sta = True
            hay_t = False

print("a.Cantidad total de palabras:", ctp)
print("b.Cantidad de palabras que inician con 'p':", cpp)
print("c.Cantidad de palabras que contienen 'ta':", cta)
