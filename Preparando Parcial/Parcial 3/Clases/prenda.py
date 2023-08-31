class Prenda:
    def __init__(self, num, desc, precio, stock, tipo):
        self.numero = num
        self.descripcion = desc
        self.precio = precio
        self.stock = stock
        self.tipo = tipo


def to_string(prenda):
    r = ""
    r += "{:<25}".format("Número de Prenda: " + str(prenda.numero))
    r += "{:<40}".format("Descripción: " + prenda.descripcion)
    r += "{:<15}".format("Precio: " + str(prenda.precio))
    r += "{:<30}".format("Stock: " + str(prenda.stock))
    r += "{:<25}".format("Tipo: " + str(prenda.tipo))

    return r
