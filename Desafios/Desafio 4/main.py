import os
import pickle
import math

class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def read_FD(FD):
    v = []
    m = open(FD, "rb")
    size = os.path.getsize(FD)

    while m.tell() < size:
        p = pickle.load(m)
        v.append(p)

    m.close()
    return v


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))

def buscar_d(v):
    d_max = 0
    d_min = distance_between(v[0], v[1])
    n = 5000
    for i in range(n-1):
        for j in range(i+1, n):
            d = distance_between(v[i], v[j])
            if d < d_min:
                d_min = d
            if d > d_max:
                d_max = d
    return d_min, d_max

def test():
    # Pasar del archivo a un vector
    FD = "puntos.df4"
    vector = read_FD(FD)
    print("Lectura Completada")

    print("Buscando...")

    d_min, d_max = buscar_d(vector)

    print("Distancia Mínima: ", round(d_min, 0))
    print("Distancia Máxima: ", round(d_max, 0))


if __name__ == "__main__":
    test()
