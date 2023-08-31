# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable
# de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para
# indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio
# en blanco. El programa debe incluir al menos una función simple con parámetros y retorno de resultado,
# debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente
# sin usar un menú de opciones:

# Turno 01 – Enunciado 04 [T1E4]
# 1. Determinar cuántas palabras del texto comienzan con un dígito par. Ejemplo: "Cursé el 1er año
# en el 1k03 y el 2do año en el 2k07." Resultado: 2 Palabras ("2do" y "2k07").

# 2. Determinar el promedio de caracteres por palabra de aquellas palabras que contienen, al menos,
# 2 vocales. (en mayúscula o minúscula). Ejemplo: "Definitivamente voy a aprobar este parcial. Las
# palabras que cumplen la condición son "Definitivamente", "aprobar", "este" y "parcial".  Son 4 palabras
# que suman 33 caracteres, y por lo tanto el promedio es 8.25. Por "caracteres", se entiende "cualquier tipo
# de símbolo, sea este un dígito, una letra, o cualquier otro que pueda aparecer".

# 3. Determinar cuántas palabras que, estando en posición impar (1ra palabra, 3ra palabra, etc.), contienen
# un número par de vocales (mayúsculas o minúsculas). Ejemplo: "Este es un simple texto de prueba."
# Resultado: 2 Palabras ("Este" y "texto", que son la primera y la quinta).

# 4. Determinar el porcentaje que representan las palabras que terminan con la expresión "no".
# Ejemplo: "Mariano no pudo obtener el disco de platino." Resultado: Las palabras que cumplen son "Mariano",
# "no" y "platino". Son 3 palabras en un total de 8, por lo que el porcentaje es 37.5%.

def es_digitopar(car):
    res = False
    if car in "24680":
        res = True
    return res


def es_vocal(car):
    res = False
    if car in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        res = True
    return res


def promedio(cantidad, total):
    avg = 0
    if total > 0:
        avg = round(cantidad / total, 2)
    return avg


def porcentaje(subtotal, total):
    if total > 0:
        porc = round(subtotal * 100 / total, 2)
    else:
        porc = 0
    return porc


def principal():
    # Contadores de caracteres y palabras
    ccar = cpal = 0

    # Contador y Banderas para palabras con dígitos par
    dig_par = False
    cpal_digp = 0

    # Contadores para analizar palabras con vocales
    cvoc = ctotal_car = 0
    cpal_2voc = 0

    cpal_impar_vpar = 0

    # Contadores y banderas para palabras terminadas en 'no'
    tiene_n = tiene_no = False
    pos_n = penultima = 0
    cpal_tno = 0

    print("Programa de análisis de texto con funciones")

    texto = input("Ingrese un texto (termina con punto):")

    for car in texto:
        if car != " " and car != ".":
            ccar += 1
            if ccar == 1 and es_digitopar(car):
                dig_par = True

            if es_vocal(car):
                cvoc += 1

            if car == "n":
                tiene_n = True
                pos_n = ccar
            else:
                if tiene_n and car == "o":
                    tiene_no = True
                tiene_n = False

            penultima = ccar - 1
        else:
            if ccar > 0:
                cpal += 1
                if dig_par:
                    cpal_digp += 1

                if cvoc >= 2:
                    ctotal_car += ccar
                    cpal_2voc += 1

                if cpal % 2 == 1 and cvoc > 0 and cvoc % 2 == 0:
                    cpal_impar_vpar += 1

                if tiene_no and pos_n == penultima:
                    cpal_tno += 1

                # Reinicio de contadores y banderas
                dig_par = False
                ccar = 0
                cvoc = 0
                pos_n = 0
                tiene_n = tiene_no = False

    # Promedio de caracteres por palabra cuando tienen 2 o más vocales
    prom_2voc = promedio(ctotal_car, cpal_2voc)

    # Porcentaje de palabras terminadas en 'no'
    porc_pal_tno = porcentaje(cpal_tno, cpal)

    print("======RESULTADOS======")
    print("Cantidad de palabras que comienzan con dígito par:", cpal_digp)
    print("Promedio de caracteres por palabra de aquellas con al menos 2 vocales:", prom_2voc)
    print("Cantidad de palabras en posición impar y con cantidad de vocales par:", cpal_impar_vpar)
    print("Porcentaje de palabras terminadas en 'no':", str(porc_pal_tno) + "%")


if __name__ == "__main__":
    principal()
