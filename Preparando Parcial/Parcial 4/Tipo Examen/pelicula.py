class Pelicula:
    def __init__(self, num, tit, imp, tipo, pais):
        self.numero = num
        self.titulo = tit
        self.importe = imp
        self.tipo = tipo
        self.pais = pais

def to_string(pelicula):
    r = ""
    r += "{:<25}".format("Número: " + str(pelicula.numero))
    r += "{:<20}".format("Título: " + pelicula.titulo)
    r += "{:<25}".format("Importe: " + str(pelicula.importe))
    r += "{:<20}".format("Tipo: " + str(pelicula.tipo))
    r += "{:<25}".format("País: " + str(pelicula.pais))

    return r
