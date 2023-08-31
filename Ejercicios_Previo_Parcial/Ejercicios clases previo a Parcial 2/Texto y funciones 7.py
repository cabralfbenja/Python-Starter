# 1) - Determinar la cantidad de palabras que contiene la letra “l” en la primera mitad de la palabra
# y terminan con “s”. Por ejemplo, en el texto: “Los elementos allanados seran totalizados en el juzgado.”
# Tiene 2 palabras que cumplen con la condición “elementos” y “allanados”.
# 2) - Determinar el porcentaje que representan las palabras de longitud impar con respecto del total de
# palabras del texto. Por ejemplo, en el texto: “La carta se entrega en el correo por la mañana.” Tiene 3
# palabras de longitud impar, hay 10 palabras del texto es de, el porcentaje seria 3 / 10 = 33.33 %.
# 3) - Determinar la cantidad de palabras que contiene la secuencia “pl” a partir de la tercer letra.
# Por ejemplo, en el texto : “El empleado tenia que emplear un pegamento para unir el plegado.” Tiene 2 palabras
# que cumplen con la condición “empleado” y “emplear”.
# 4) - Determinar la cantidad de palabras que tiene una mayor cantidad de digitos que letras, pero
# dicha palabra debe contener al menos una letra. Por ejemplo, en el texto: “Los cursos 1K09 y 1K15 son espejos desde el 2020.” Tiene 2 palabras que cumplen con la condición “1K09” y “1K15”..


def porcentaje(subtotal, total):
    if total > 0:
        porc = round(subtotal * 100 / total, 2)
    else:
        porc = 0
    return porc


def es_digito(car):
    res = False
    if car in "1234567890":
        res = True
    return res


def es_letra(car):
    res = False
    if "a" <= car <= "z" or "A" <= car <= "Z":
        res = True
    return res


def test():
    # Contadores
    clet = 0
    cls = 0
    cpal = 0
    cpal_impar = 0
    cpal_pl3 = 0
    c_dig = c_letras = cpal_dig_let = 0
    # Banderas
    ban_l = False
    primera_l = True
    ban_p = ban_pl = False

    pos_l = 0
    ultima = ""

    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car != " " and car != ".":
            clet += 1
            if car == "l":
                if primera_l:
                    pos_l = clet
                    primera_l = False
            if clet >= 3:
                if car == "p":
                    ban_p = True
                else:
                    if car == "l" and ban_p:
                        ban_pl = True
                    ban_p = False
            if es_digito(car):
                c_dig += 1
            elif es_letra(car):
                c_letras += 1

            ultima = car
        else:
            if clet > 0:
                cpal += 1
                if clet % 2 == 1:
                    cpal_impar += 1
                medio = clet // 2
                if ultima == "s" and 0 < pos_l < medio:
                    cls += 1
                if ban_pl:
                    cpal_pl3 += 1
                if 0 < c_letras < c_dig:
                    cpal_dig_let += 1

                # REINICIO
                clet = c_dig = c_letras = 0
                pos_l = 0
                primera_l = True
                ban_pl = ban_p = False

    pct_impar = porcentaje(cpal_impar, cpal)
    print("======RESULTADOS======")
    print("Cantidad de palabras que contienen la letra 'l' en la primera mitad y terminan con 's':", cls)
    print("Porcentaje de palabras impares en el texto:", pct_impar, "%")
    print("Cantidad de palabras que contienen la secuencia 'pl' a partir de la tercer letra:", cpal_pl3)
    print("Cantidad de palabras con más dígitos que letras y con al menos una letra:", cpal_dig_let)


if __name__ == "__main__":
    test()
