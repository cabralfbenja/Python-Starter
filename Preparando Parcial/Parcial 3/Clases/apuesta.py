class Apuesta:
    def __init__(self, num, cab, monto):
        self.numero = num
        self.caballo = cab
        self.monto = monto

def to_string(apuesta):
    r = ""
    r += "{:<25}".format("Número de Ticket: " + str(apuesta.numero))
    r += "{:<25}".format("Caballo elegido: " + str(apuesta.caballo))
    r += "{:<25}".format("Monto de apuesta: " + str(apuesta.monto))
    return r
