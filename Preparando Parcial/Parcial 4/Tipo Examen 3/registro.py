class Consumo:
    def __init__(self, num, cli, mes, tipo, monto):
        self.numero = num
        self.cliente = cli
        self.mes = mes
        self.tipo = tipo
        self.monto = monto

def to_string(consumo):
    r = ""
    r += "{:<25}".format("Número: " + str(consumo.numero))
    r += "{:<20}".format("Cliente: " + consumo.cliente)
    r += "{:<25}".format("Mes: " + str(consumo.mes))
    r += "{:<20}".format("Tipo: " + str(consumo.tipo))
    r += "{:<25}".format("Monto: " + str(consumo.monto))

    return r
