"""
2. Mejores alumnos
En un colegio secundario se maneja la información de las notas de una materia con tres vectores de longitud n,
 llamados trim1, trim2 y trim3. Esos vectores almacenan las notas correspondientes a cada trimestre para cada alumno.
  Asimismo se mantienen los nombres de los alumnos en otro vector paralelo a los de las notas.

Se necesita un programa que permita ingresar todos esos datos y que luego de la carga genere un cuarto vector
 que contenga el promedio de cada alumno. Finalmente el programa debe mostrar todos los datos de los tres alumnos
  con mejor promedio de la materia.
"""
import random

def validar(inf):
    n = int(input("Valor (mayor a "+ str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error...se pidió > " + str(inf) + " ...Cargue de nuevo: "))
    return n


def carga(n):
    trim1 = [0] * n
    trim2 = [0] * n
    trim3 = [0] * n
    alumno = [""] * n
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    apellido = ["Gomez", "Marquez", "Farré", "Hora", "Juira", "Mola", "Wembor"]

    for i in range(n):
        alumno[i] = random.choice(alfabeto) + "." + random.choice(apellido)
        trim1[i] = random.randint(1, 10)
        trim2[i] = random.randint(1, 10)
        trim3[i] = random.randint(1, 10)
    return trim1, trim2, trim3, alumno

def avg(t1,t2, t3, n):
    promedios = [0] * n

    for i in range(n):
        suma = t1[i] + t2[i] + t3[i]
        promedios[i] = round(suma / 3, 2)
    return promedios


def selection_sort(t1, t2, t3, alu, pro):
    n = len(t1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pro[j] > pro[i]:
                t1[i], t1[j] = t1[j], t1[i]
                t2[i], t2[j] = t2[j], t2[i]
                t3[i], t3[j] = t3[j], t3[i]
                alu[i], alu[j] = alu[j], alu[i]
                pro[i], pro[j] = pro[j], pro[i]

def best_avg(t1, t2, t3, alumno, promedios):
    selection_sort(t1, t2, t3, alumno, promedios)

    print("Alumno", end=" | ")
    print("T1", end=" | ")
    print("T2", end=" | ")
    print("T3", end=" | ")
    print("Promedio")



    for i in range(3):
        print(alumno[i], end=" | ")
        print(t1[i], end=" | ")
        print(t2[i], end=" | ")
        print(t3[i], end=" | ")
        print(promedios[i])


def principal():
    print("REGISTRO DE NOTAS")
    print("Ingrese la cantidad de Alumnos")
    n = validar(0)

    trim1, trim2, trim3, alumno = carga(n)

    promedios = avg(trim1, trim2, trim3, n)

    print(alumno)
    print(trim1)
    print(trim2)
    print(trim3)
    print(promedios)

    best_avg(trim1, trim2, trim3, alumno, promedios)




if __name__ == "__main__":
    principal()
