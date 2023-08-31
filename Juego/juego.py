class Juego:
    def __init__(self, cod, nombre, precio, edad, sector):
        self.codigo = cod
        self.nombre = nombre
        self.precio = precio
        self.edad = edad
        self.sector = sector

def to_string(juego):
    r = ""
    r += "{:<20}".format("Código: " + str(juego.codigo))
    r += "{:<30}".format("Nombre: " + juego.nombre)
    r += "{:<20}".format("Precio: " + str(juego.precio))
    r += "{:<20}".format("Edad mínima: " + str(juego.edad))
    r += "{:<25}".format("Sector: " + str(juego.sector))

    return r

