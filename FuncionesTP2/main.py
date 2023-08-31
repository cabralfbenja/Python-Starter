def ganador(n1, n2):
    if n1 > n2:
        res = 1
    elif n2 > n1:
        res = 2
    else:
        res = 3
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


