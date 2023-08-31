from random import randint


for i in range(10):
    print("Prueba", i+1)
    x = randint(100, 800)
    dist = randint(0, 300)
    while x - dist < 0 or x + dist > 900:
        print(dist)
        dist = randint(0, dist)
    lim_izq = x - dist
    lim_der = x + dist
    print(x, dist, end="-----")
    print("(",lim_izq,",", lim_der,")")
