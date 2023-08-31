class Proyecto:
    def __init__(self, num, cliente, hon, tipo):
        self.numero = num
        self.cliente = cliente
        self.honorarios = hon
        self.tipo = tipo

def to_string(proyecto):
    r = ""
    r += "{:<25}".format("Número de Proyecto: " + str(proyecto.numero))
    r += "{:<30}".format("Cliente: " + proyecto.cliente)
    r += "{:<25}".format("Honorarios: " + str(proyecto.honorarios))
    r += "{:<15}".format("Tipo: " + str(proyecto.tipo))

    return r
