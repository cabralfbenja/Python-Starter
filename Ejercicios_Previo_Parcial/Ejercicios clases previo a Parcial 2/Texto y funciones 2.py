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


def average(suma, cant):
    if cant > 0:
        prom = suma / cant
    else:
        prom = 0
    return prom


def test():
    # "SI"
    ban_s = ban_si = False
    cpal_si = cl = 0

    # Termina con vocal
    ultima_letra = " "
    cpal_tvi = 0

    # Cant de vocales en una palabra
    cant_voc = cpal_voc = 0

    # Palabras con primera y última iguales
    cpal_pyu = 0
    primera_letra = " "

    # Expresion cc
    ban_cc = False
    cont_c = cpal_cc = 0

    # Palabra más corta
    pal_min = 0
    # Cantidad total de palabras y letras
    cpal = ctl = 0
    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                cpal += 1
                ctl += cl
            # Longitud de la palabra más corta
            if cpal == 1 or cl < pal_min:
                pal_min = cl

            # Cantidad de palabras que comienzan con "si"
            if ban_si:
                cpal_si += 1

            # Cantidad de palabras que terminan en vocal y cantidad impar de letras
            if es_vocal(ultima_letra) and cl % 2 == 1:
                cpal_tvi += 1

            # Cantidad de palabras con una sola vocal
            if cant_voc == 1:
                cpal_voc += 1

            # Cantidad de palabras que comienzan y terminan con la misma letra
            if primera_letra == ultima_letra:
                cpal_pyu += 1

            # Cantitad de palabras con "cc"
            if ban_cc:
                cpal_cc += 1

            ban_s = ban_si = ban_cc = False
            cl = cont_c = 0

        else:
            cl += 1
            if cl == 1:
                primera_letra = car

            if car == "s" and cl == 1:
                ban_s = True
            else:
                if car == "i" and ban_s:
                    ban_si = True
                ban_s = False

            if es_vocal(car):
                cant_voc += 1

            if car == "c":
                cont_c += 1
                if cont_c == 2:
                    ban_cc = True
            else:
                cont_c = 0
            ultima_letra = car

    porc_tvi = porcentaje(cpal_tvi, cpal)
    promedio = average(ctl, cpal)
    print("Cantidad de palabras que comienzan con 'si':", cpal_si)
    print("Cantidad de palabras que terminan en vocal y su cantidad de letras es impar:", cpal_tvi)
    print("Cantidad de palabras con una sola vocal:", cpal_voc)
    print("Cantidad de palabras que comienzan y terminan con la misma letra:", cpal_pyu)
    print("Cantidad de palabras que contienen 'cc':", cpal_cc)
    print("Porcentaje de palabras que terminan en vocal, con cantidad de letras impar:", porc_tvi, "%")
    print("Longitud de la palabra más corta:", pal_min)
    print("La cantidad promedio de letras por palabra es:", promedio)


test()
