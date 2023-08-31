class Vacunacion:
    def __init__(self, nom, vac, pri, seg):
        self.jurisdiccion = nom
        self.vacuna = vac
        self.cantidad_primera = pri
        self.cantidad_segunda = seg

def to_string(vacunacion):
    r = ""
    r += "{:<25}".format("Jurisdicción: " + vacunacion.jurisdiccion)
    r += "{:<40}".format("Vacuna: " + vacunacion.vacuna)
    r += "{:<25}".format("Cantidad Primera: " + str(vacunacion.cantidad_primera))
    r += "{:<25}".format("Cantidad Segunda: " + str(vacunacion.cantidad_segunda))

    return r
def to_string_con_total(vacunacion):
    r = ""
    r += "{:<25}".format("Jurisdicción: " + vacunacion.jurisdiccion)
    r += "{:<20}".format("Vacuna: " + vacunacion.vacuna)
    r += "{:<25}".format("Cantidad Primera: " + str(vacunacion.cantidad_primera))
    r += "{:<25}".format("Cantidad Segunda: " + str(vacunacion.cantidad_segunda))
    suma =  vacunacion.cantidad_primera + vacunacion.cantidad_segunda
    r += "{:<25}".format("Total de Dosis: " + str(suma))
    return r
