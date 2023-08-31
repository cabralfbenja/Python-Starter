# 1 - Determinar la cantidad de palabras que terminan con la tercer letra de la primera palabra del texto. Por ejemplo,
# en el texto: “Las casas se terminaron antes de lo previsto.” Tiene 2 palabras que cumplen con la condición: “casas” y
# “antes”.
#   2 - Determinar la cantidad palabras que tienen vocales en la segunda mitad de la palabra y cuya longitud sea mayor o
#   igual a 5 letras. Por ejemplo, en el texto “Las materias de la facultad en cuarentena se rinden en aula virtual.”
#   Tiene 5 palabras que cumplen con la condición: “materias”, “facultad”, “rinden”, ”cuarentena” y “virtual”.
#   3 - Determinar la cantidad de palabras de longitud impar que se encuentran en el texto y que comienzan con una
#   consonante. Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.” Tiene 2 palabras que cumplen
#   con la condición: “virtual” y “realizan”.
#   4 - Determinar el porcentaje que representan las palabras del punto 3 en base al total de palabras que se encuentran
#   en el texto. Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.” La cantidad de palabras son
#   8, 2 palabras cumplen con el punto 3, el porcentaje seria 2/8 = 25%.

def es_vocal(car):
    res = False
    if car in "aeiouAEIOU":
        res = True
    return res


def porcentaje(subtotal, total):
    if total > 0:
        porc = round(subtotal * 100 / total, 2)
    else:
        porc = 0
    return porc


def test():
    clet = cpal = c_pal3 = pos_vocal = c_palvoc5 = cp_icons = 0
    tercera_let = ultima_let = ""
    primera_let = False

    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car == " " or car == ".":
            if clet > 0:
                cpal += 1

            if cpal > 1 and ultima_let == tercera_let:
                c_pal3 += 1

            medio = clet // 2

            if pos_vocal >= medio and clet >= 5:
                c_palvoc5 += 1

            if not primera_let and clet % 2 == 1:
                cp_icons += 1

            clet = 0
        else:
            clet += 1
            if clet == 1:
                primera_let = es_vocal(car)

            if clet == 3 and cpal == 0:
                tercera_let = car

            if es_vocal(car):
                pos_vocal = clet

            ultima_let = car

    porc_icons = porcentaje(cp_icons, cpal)

    print("\nCantidad de palabras que terminan con la tercer letra de la primera palabra del texto:", c_pal3)
    print("Cantidad palabras que tienen vocales en la segunda mitad de la palabra y "
          "cuya longitud es mayor o igual a 5:", c_palvoc5)
    print("Cantidad de palabras de longitud impar y comienzan con una consonante:", cp_icons)
    print("Porcentaje de palabras de longitud impar y comienzan con una consonante:", porc_icons, "%")


if __name__ == "__main__":
    test()
