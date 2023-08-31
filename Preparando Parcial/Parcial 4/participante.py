class Participante:
    def __init__(self, cod, apellido, loc, disc, punt):
        self.codigo = cod
        self.apellido = apellido
        self.localidad = loc
        self.disciplina = disc
        self.puntaje = punt


def to_string(participante):
    r = ""
    r += "{:<25}".format("Código: " + participante.codigo)
    r += "{:<20}".format("Apellido: " + participante.apellido)
    r += "{:<20}".format("Localidad: " + str(participante.localidad))
    r += "{:<20}".format("Disciplina: " + str(participante.disciplina))
    r += "{:<25}".format("Puntaje: " + str(participante.puntaje))

    return r
