from voto import *
from candidato import *
import random
import pickle
import os.path

def generar_sin_repetir(m):
    a = 1
    while a == 1:
        a = 0
        votante = random.randint(0, 99999)
        for i in range(len(m)):
            if a == m[i]:
                a = 1

    return votante

def alta():
    m = open("votos.dat", "wb")
    votante = []
    for i in range(300):
        v = Voto(random.randint(0, 6), random.randint(0, 20), generar_sin_repetir(votante))
        pickle.dump(v, m)
        m.flush()
    m.close()

def alta_candidato():
    m = open("candidatos.dat", "wb")
    nom = ("Juan Manolas", "Carlos Andorra", "Benjamín Cabral", "Mateo Vaotrez", "Esteban Kierat", "Marcos Aurelio",
               "Mariano Max")

    for i in range(7):
        v = Candidato(i, nom[i])
        pickle.dump(v, m)
        m.flush()

    m.close()

alta()
alta_candidato()
