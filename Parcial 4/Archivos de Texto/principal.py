from registro import *

def generar_vector():
    vec_vacunacion = []
    m = open("Covid19VacunasAgrupadas.csv", encoding="UTF-8")
    primera_linea = True
    for linea in m:
        if primera_linea:
            primera_linea = False
            continue
        if linea[-1] == "\n":
            linea = linea[:-1]
        cadena = linea.split(",")
        jur = cadena[1]
        vac = cadena[2]
        pri = int(cadena[3])
        seg = int(cadena[4])
        vacunacion = Vacunacion(jur, vac, pri, seg)
        vec_vacunacion.append(vacunacion)

    m.close()
    return vec_vacunacion

def mostrar_vector(v):
    for reg in v:
        print(to_string(reg))

def test():
    vec_vacunacion = generar_vector()
    mostrar_vector(vec_vacunacion)


if __name__ == "__main__":
    test()

