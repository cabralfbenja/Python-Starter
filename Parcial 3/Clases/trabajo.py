class Trabajo:
    def __init__(self, id, nom, tipo, imp, cant):
        self.numero= id
        self.descripcion = nom
        self.tipo = tipo
        self.importe = imp
        self.cantidad = cant

def to_string(trabajo):
    r = ""
    r += "{:<25}".format("Número de Trabajo: " + str(trabajo.numero))
    r += "{:<40}".format("Descripción: " + trabajo.descripcion)
    r += "{:<15}".format("Tipo: " + str(trabajo.tipo))
    r += "{:<30}".format("Importe: " + str(trabajo.importe))
    r += "{:<25}".format("Cantidad de empleados: " + str(trabajo.cantidad))

    return r
