def sucesion(n):
    if n % 2 == 0:
        res = n/2
    else:
        res = 3 * n + 1
    return res

def promedio(suma, cant):
    pr = round(suma / cant, 1)
    return pr


n = int(input("n = "))
orbita = [n]

while n != 1:
    n = sucesion(n)
    orbita[len(orbita):] = [n]

lon = len(orbita)


ac = 0
for i in range(lon):
    ac += orbita[i]
prom = promedio(ac, lon)

maxim = max(orbita)

print("Sucesión:", orbita)
print("Longitud:", lon)
print("Promedio:", prom)
print("Mayor:", maxim)


