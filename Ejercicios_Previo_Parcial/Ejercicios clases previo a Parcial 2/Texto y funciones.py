def es_vocal(car):
    res = False
    if car in "aeiou":
        res = True
    return res

def porcentaje(subtotal, total):
    if total > 0:
        porc = round(subtotal * 100 / total, 2)
    else:
        porc = 0
    return porc

def test():
    # Contadores y Banderas
    cdp = pal_a = 0
    letras_palabra = 0
    longitud_max = None
    ban_a = ban_eiou = False

    print("Programa de análisis de texto con funciones")
    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:

        if car == " " or car == ".":
            cdp += 1
            if cdp == 1 or letras_palabra > longitud_max:
                longitud_max = letras_palabra

            if ban_a and not ban_eiou:
                pal_a += 1

            # Reinicio de variables
            letras_palabra = 0
            ban_eiou = ban_a = False

        else:
            letras_palabra += 1

            if es_vocal(car):
                if car == "a":
                    ban_a = True
                else:
                    ban_eiou = True
    # Porcentaje
    p = porcentaje(pal_a, cdp)

    print("Longitud de la palabra más larga:", longitud_max)
    print("Cantidad de palabras con solo la vocal 'a':", pal_a)
    print("Porcentaje que representan:", p, "%")

test()
