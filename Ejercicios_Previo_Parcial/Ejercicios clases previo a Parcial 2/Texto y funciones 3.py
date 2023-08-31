import Soporte


def test():
    # Vocal
    b_vocal = False
    c_palv = 0

    # SA en la primer mitad
    b_s = False
    b_sa = False
    cl = 0
    c_palsa = 0
    punto = 0

    c_par = 0
    c_pal = 0

    ban_car = False
    especial = None
    c_palesp = 0

    pal_larga = pos = 0
    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car == " " or car == ".":
            c_pal += 1

            # 1
            if b_vocal:
                c_palv += 1
            # 2
            mitad = cl / 2
            if b_sa and punto <= mitad:
                c_palsa += 1

            # 3
            if cl % 2 == 0:
                c_par += 1

            # 4
            if ban_car and c_pal > 1:
                c_palesp += 1

            # 5
            if c_pal == 1:
                pal_larga = cl
                pos = 1
            else:
                if cl > pal_larga:
                    pal_larga = cl
                    pos = c_pal

            # Reseteo
            cl = 0
            b_vocal = False
            b_sa = False
            b_s = False
            ban_car = False

        else:
            cl += 1
            if Soporte.es_vocal(car):
                b_vocal = True
            if car == "s":
                b_s = True
            else:
                if car == "a" and b_s and not b_sa:
                    b_sa = True
                    punto = cl - 1

                b_s = False

            if c_pal == 0:
                especial = car
            else:
                if car == especial:
                    ban_car = True

    porcentaje = Soporte.porcentaje(c_par, c_pal)

    print("Cantidad de palabras con al menos una vocal:", c_palv)
    print("Cantidad de palabras con 'sa' en la primer mitad:", c_palsa)
    print("Porcentaje de palabras con cantidad de caracteres par:", porcentaje, "%")
    print("Cantidad de palabras que cumplen la condición especial:", c_palesp)
    print("Longitud de la palabra más larga:", pal_larga)
    print("Posición de la palbra más larga:", pos)


if __name__ == "__main__":
    test()
