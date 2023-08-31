def es_vocal(car):
    res = False
    if car in "aeiouAEIOU":
        res = True
    return res


def es_digito(car):
    res = False
    if car in "1234567890":
        res = True
    return res


def porcentaje(subtotal, total):
    if total > 0:
        porc = round(subtotal * 100 / total, 2)
    else:
        porc = 0
    return porc


def test():
    cl = c_voc3 = cp = c_pald = c_lapar = menor = 0

    b_voc = b_dig = bl = b_la = False

    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                cp += 1

            if cp == 1 or menor > cl:
                menor = cl

            if cl > 3 and b_voc:
                c_voc3 += 1

            if b_dig:
                c_pald += 1

            if b_la and cl % 2 == 0:
                c_lapar += 1

            cl = 0
            b_voc = b_dig = b_la = False

        else:
            cl += 1

            if cl == 1 and es_vocal(car):
                b_voc = True

            if es_digito(car):
                b_dig = True

            if car in "lL":
                bl = True
            else:
                if car in "aA" and bl:
                    b_la = True
                bl = False

    porc_dig = porcentaje(c_pald, cp)

    print("Cantidad de palabras que inician con vocal y con más de 3 letras:", c_voc3)
    print("Porcentaje de palabras con al menos un dígito:", porc_dig, "%")
    print("Cantidad de palabras con 'la' y cantidad par de letras:", c_lapar)
    print("La longitud de la palabra más corta es:", menor)


if __name__ == "__main__":
    test()
