class Voto:
    def __init__(self, cand, prov, dni):
        self.candidato = cand
        self.provincia = prov
        self.votante = dni

def to_string(voto):
    r = ""
    r += "{:<25}".format("Candidato: " + str(voto.candidato))
    r += "{:<25}".format("Provincia: " + str(voto.provincia))
    r += "{:<25}".format("Votante: " + str(voto.votante))

    return r
