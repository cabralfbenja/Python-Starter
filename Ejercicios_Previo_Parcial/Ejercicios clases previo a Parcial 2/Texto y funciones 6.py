# 1 - Determinar la cantidad de palabras que presentan digitos en la palabra. Por ejemplo, en el texto:
# “El 1K09 y el 1K15 son cursos espejos a partir del año 2020.” Tiene 3 palabras que cumplen con la condición: “1K09”,
# “1K15” y “2020”.
# 2 - Determinar el promedio de letras de la palabras del texto que presentan la combinacion “pe” a partir
# de la tercer letra de la palabra. Por ejemplo, en el texto: “El acampe del año apenas tuvo un ágape.” Tiene
# 2 palabras que cumplen con la condición “acampe” y “ágape” que suman 11 letras, por lo que el promedio seria
# 11/2 = 5.5 letras.
# 3 - Determinar la cantidad de palabras que finalizan con la letra “n” y que empiecen con una vocal. Por ejemplo,
# en el texto: “Los jovenes acamparon y asaron unos choripanes.” Tiene 2 palabras que cumplen con la condición
# “acamparon” y “asaron”.
# 4 - Determinar la cantidad de palabras que finalizan con la primera letra de esa palabra. Por ejemplo, en el
# texto: “Las simples vidas son solitarias.” Tiene 2 palabras que cumplen con la condición “simples” y “solitarias”.

def es_digito(car):
    res = False
    if car in "1234567890":
        res = True
    return res


def es_vocal(car):
    res = False
    if car in "aeiouAEIOU":
        res = True
    return res


def promedio(cantidad, total):
    avg = 0
    if total > 0:
        avg = cantidad / total
    return avg


def test():
    # Banderas
    digito = False
    ban_p = ban_pe = False
    primera_voc = False

    # Contadores
    cp_dig = 0
    clet = cpal = 0
    cp_pe = 0
    cp_vocn = 0
    cp_pr_ult = 0

    # Acumulador de letras, punto 2
    acu_let = 0
    # Variable para revisar primera y última letra
    primera = ultima = ""

    print("Análisis de Texto")
    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car != " " and car != ".":
            clet += 1

            if clet == 1:
                if es_vocal(car):
                    primera_voc = True
                primera = car

            if es_digito(car):
                digito = True

            if clet >= 3:
                if car == "p":
                    ban_p = True
                else:
                    if car == "e" and ban_p:
                        ban_pe = True
                    ban_p = False
            ultima = car

        else:
            cpal += 1
            if digito:
                cp_dig += 1
            if ban_pe:
                acu_let += clet
                cp_pe += 1

            if primera_voc and ultima == "n":
                cp_vocn += 1

            if primera == ultima:
                cp_pr_ult += 1

            # Reinicio
            ban_p = ban_pe = False
            digito = False
            clet = 0

    prom_lpe = promedio(acu_let, cp_pe)
    print("======RESULTADOS======")
    print("Cantidad de palabras con dígitos:", cp_dig)
    print("Promedio de letras de palabras que presentan “pe” a partir de la tercer letra:", prom_lpe)
    print("Cantidad de palabras que comienzan con vocal y terminan con 'n':", cp_vocn)
    print("Cantidad de palabras que comienzan y terminan con la misma letra:", cp_pr_ult)


if __name__ == "__main__":
    test()
