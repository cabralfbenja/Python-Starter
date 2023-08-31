class Envio:
    def __init__(self, num, desc, monto, prov, tipo, barrio):
        self.id = num
        self.descripcion = desc
        self.monto = monto
        self.provincia = prov
        self.tipo = tipo
        self.barrio = barrio

def to_string(envio):
    r = ""
    r += "{:<25}".format("ID: " + str(envio.id))
    r += "{:<30}".format("Descripción: " + envio.descripcion)
    r += "{:<25}".format("Monto: " + str(envio.monto))
    r += "{:<20}".format("Provincia: " + str(envio.provincia))
    r += "{:<15}".format("Artículo: " + str(envio.tipo))
    r += "{:<30}".format("Barrio: " + envio.barrio)

    return r
