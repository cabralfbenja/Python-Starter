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

def es_digito(car):
    res = False
    if car in "1234567890":
        res = True
    return res

def promedio(cantidad, total):
    avg = 0
    if total > 0:
        avg = cantidad / total
    return avg


def test():
    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

     for car in texto:
        if car != " " and car != ".":
            pass
        else:
            pass


if __name__ == "__main__":
    test()
